from fastapi import FastAPI, Depends, HTTPException, status, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, Session
from werkzeug.security import generate_password_hash, check_password_hash
from pydantic import BaseModel
from sqlalchemy.sql import text
from fastapi import HTTPException, Depends, status
import jwt
from datetime import datetime, timedelta
from fastapi import HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer



DATABASE_URL = "postgresql://postgres:password@db:5432/internships_db"


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


app = FastAPI()


TEMPLATES_PATH = "/app/Frontend"
templates = Jinja2Templates(directory=TEMPLATES_PATH)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class InternshipCreate(BaseModel):
    title: str
    company_name: str
    start_date: str
    end_date: str = None
    application_link: str
    status: str



@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    user_id = request.cookies.get("user_id")
    if not user_id:
        return RedirectResponse(url="/login")
    return RedirectResponse(url="/dashboard")


@app.get("/register", response_class=HTMLResponse)
async def show_register_page(request: Request):
    user_id = request.cookies.get("user_id")
    if user_id:
        return RedirectResponse(url="/dashboard")


    error_message = request.query_params.get("error_message")
    return templates.TemplateResponse("register.html", {"request": request, "error_message": error_message})


@app.post("/register/")
def register(
        username: str = Form(...),
        email: str = Form(...),
        password: str = Form(...),
        db: Session = Depends(get_db)
):
    db_user = db.execute(text("SELECT * FROM Users WHERE email = :email"), {"email": email}).fetchone()

    if db_user:

        return RedirectResponse(url="/register?error_message=User already exists", status_code=303)

    hashed_password = generate_password_hash(password, method="pbkdf2:sha256")

    db.execute(
        text("INSERT INTO Users (username, email, password) VALUES (:username, :email, :password)"),
        {"username": username, "email": email, "password": hashed_password}
    )
    db.commit()
    return RedirectResponse(url="/login", status_code=302)



@app.get("/login", response_class=HTMLResponse)
async def show_login_page(request: Request):
    user_id = request.cookies.get("user_id")
    if user_id:
        return RedirectResponse(url="/dashboard")
    return templates.TemplateResponse("login.html", {"request": request})


@app.post("/login/")
def login(
        email: str = Form(...),
        password: str = Form(...),
        db: Session = Depends(get_db)
):
    user = db.execute(text("SELECT * FROM Users WHERE email = :email"), {"email": email}).fetchone()

    if not user or not check_password_hash(user.password, password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    response = RedirectResponse(url="/dashboard", status_code=303)
    response.set_cookie(key="user_id", value=user.id)
    return response


@app.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request, db: Session = Depends(get_db)):
    user_id = request.cookies.get("user_id")
    if not user_id:
        return RedirectResponse(url="/login", status_code=303)
    internships = db.execute(
        text("SELECT * FROM Internship WHERE user_id = :user_id"),
        {"user_id": user_id}
    ).fetchall()
    return templates.TemplateResponse("dashboard.html", {"request": request, "internships": internships})


@app.get("/logout")
def logout():
    response = RedirectResponse(url="/login", status_code=302)
    response.delete_cookie("user_id")
    return response


@app.get("/add_internship", response_class=HTMLResponse)
def add_internship_page(request: Request):
    user_id = request.cookies.get("user_id")
    if not user_id:
        return RedirectResponse(url="/login", status_code=303)
    return templates.TemplateResponse("add_internship.html", {"request": request})


@app.post("/add_internship/")
def add_internship(
        request: Request,
        title: str = Form(...),
        company_name: str = Form(...),
        start_date: str = Form(...),
        end_date: str = Form(None),
        application_link: str = Form(...),
        status: str = Form(...),
        db: Session = Depends(get_db)

):
    user_id = request.cookies.get("user_id")
    if not user_id:
        raise HTTPException(status_code=403, detail="Not authenticated")
    db.execute(
        text("""
        INSERT INTO Internship (title, company_name, start_date, end_date, application_link, status, user_id)
        VALUES (:title, :company_name, :start_date, :end_date, :application_link, :status, :user_id)
        """),
        {"title": title, "company_name": company_name, "start_date": start_date, "end_date": end_date,
         "application_link": application_link, "status": status, "user_id": user_id}
    )
    db.commit()
    return RedirectResponse(url="/dashboard", status_code=303)


@app.get("/delete_internship/{internship_id}")
def delete_internship(
        request: Request,
        internship_id: int,
        db: Session = Depends(get_db)
):
    user_id = request.cookies.get("user_id")
    if not user_id:
        return RedirectResponse(url="/login", status_code=303)

    internship = db.execute(
        text("SELECT * FROM Internship WHERE id = :id AND user_id = :user_id"),
        {"id": internship_id, "user_id": user_id}
    ).fetchone()

    if not internship:
        raise HTTPException(status_code=404, detail="Internship not found")

    db.execute(text("DELETE FROM Internship WHERE id = :id"), {"id": internship_id})
    db.commit()
    return RedirectResponse(url="/dashboard", status_code=303)

@app.get("/edit_internship/{internship_id}", response_class=HTMLResponse)
async def edit_internship_page(request: Request, internship_id: int, db: Session = Depends(get_db)):
    internship = db.execute(text("SELECT * FROM Internship WHERE id = :id"), {"id": internship_id}).fetchone()
    if not internship:
        raise HTTPException(status_code=404, detail="Internship not found")
    return templates.TemplateResponse("edit_internship.html", {"request": request, "internship": internship})

@app.post("/edit_internship/{internship_id}")
async def edit_internship(internship_id: int, title: str = Form(...), company_name: str = Form(...),
                           start_date: str = Form(...), end_date: str = Form(None), status: str = Form(...),
                           db: Session = Depends(get_db)):
    db.execute(
        text("""
            UPDATE Internship 
            SET title = :title, company_name = :company_name, start_date = :start_date, 
                end_date = :end_date, status = :status
            WHERE id = :id
        """),
        {"title": title, "company_name": company_name, "start_date": start_date, "end_date": end_date, "status": status, "id": internship_id}
    )
    db.commit()
    return RedirectResponse(url=f"/dashboard", status_code=303)

@app.get("/view-all-db-page", response_class=HTMLResponse)
async def view_all_db_page(request: Request):
    connection = engine.connect()
    metadata = MetaData()
    metadata.reflect(bind=engine)
    data = {}
    for table_name in metadata.tables.keys():
        table = metadata.tables[table_name]
        rows = connection.execute(table.select()).fetchall()
        data[table_name] = [dict(row._mapping) for row in rows]
    return templates.TemplateResponse("view_all_db.html", {"request": request, "data": data})


SECRET_KEY = "votre_clé_secrète"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Durée de validité du token en minutes

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Fonction pour créer un token JWT
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Fonction pour vérifier le token JWT
def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        print("[DEBUG] Vérification du token:", token)  # Ajout de logs
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.PyJWTError as e:
        print("[ERROR] Erreur de vérification du token:", str(e))  # Log des erreurs
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )



@app.get("/profile", response_class=HTMLResponse)
async def get_profile(request: Request, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        print("[DEBUG] Token reçu :", token)
        payload = verify_token(token)
        user_id = payload.get("user_id")
        print("[DEBUG] Payload décodé :", payload)
        if not user_id:
            raise HTTPException(status_code=400, detail="Invalid token: user_id missing")
    except Exception as e:
        print("[ERROR] Erreur lors de la vérification du token :", e)
        raise HTTPException(status_code=401, detail="Unauthorized")

    user = db.execute(text("SELECT * FROM Users WHERE id = :id"), {"id": user_id}).fetchone()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return templates.TemplateResponse("profile.html", {"request": request, "user": user})





@app.post("/update_profile", response_class=HTMLResponse)
async def update_profile(request: Request, token: str = Depends(oauth2_scheme),
                         username: str = Form(...), email: str = Form(...),
                         password: str = Form(...), db: Session = Depends(get_db)):
    payload = verify_token(token)
    user_id = payload.get("user_id")

    # Vérifiez si l'utilisateur existe
    db_user = db.execute(text("SELECT * FROM Users WHERE id = :id"), {"id": user_id}).fetchone()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    # Mise à jour des informations
    hashed_password = generate_password_hash(password, method="pbkdf2:sha256")
    db.execute(text("""
        UPDATE Users 
        SET username = :username, email = :email, password = :password 
        WHERE id = :id
    """), {"username": username, "email": email, "password": hashed_password, "id": user_id})

    db.commit()
    return RedirectResponse(url="/profile", status_code=303)

@app.post("/generate-token/")
def generate_token(user_id: int):
    token = create_access_token({"user_id": user_id})
    print("[DEBUG] Token généré :", token)
    return {"token": token}


@app.get("/set_all_passwords/{new_password}")
def set_all_passwords(new_password: str, db: Session = Depends(get_db)):
    """
    Met à jour tous les mots de passe des utilisateurs avec une valeur spécifique passée dans l'URL.
    """
    if not new_password:
        raise HTTPException(status_code=400, detail="Password cannot be empty")

    # Mettre à jour les mots de passe
    db.execute(text("""
        UPDATE Users
        SET password = :password
    """), {"password": new_password})

    db.commit()

    return {"message": f"All passwords have been updated to: {new_password}"}




# Run Uvicorn pour démarrer le serveur
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
