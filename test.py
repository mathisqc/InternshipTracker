from sqlalchemy import create_engine, text

# Configuration de la base de données
DB_USER = "postgres"
DB_PASSWORD = "password"
DB_HOST = "db"  # Modifier si le conteneur PostgreSQL utilise un autre hôte
DB_PORT = "5432"
DB_NAME = "internships_db"

# Connexion à la base de données
engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# Requêtes SQL pour insérer les données
INSERT_USERS = """
INSERT INTO Users (username, email, password)
VALUES
    ('alexandre.saiphou', 'alexandre.saiphou@edu.esiee.fr', '
pbkdf2:sha256:1000000$f9jKuaeciDywyUR6$a358e892b215920e90858d049f64038ad2d8f7a7c20d6a34ff05b1dabdf403b4'),
    ('alexis.simon', 'alexis.simon@edu.esiee.fr', '
pbkdf2:sha256:1000000$f9jKuaeciDywyUR6$a358e892b215920e90858d049f64038ad2d8f7a7c20d6a34ff05b1dabdf403b4'),
    ('alseny.yoro', 'alseny.yoro@edu.esiee.fr', '
pbkdf2:sha256:1000000$f9jKuaeciDywyUR6$a358e892b215920e90858d049f64038ad2d8f7a7c20d6a34ff05b1dabdf403b4'),
    ('antoine.dolley', 'antoine.dolley@edu.esiee.fr', '
pbkdf2:sha256:1000000$f9jKuaeciDywyUR6$a358e892b215920e90858d049f64038ad2d8f7a7c20d6a34ff05b1dabdf403b4'),
    ('antoine.merlet', 'antoine.merlet@edu.esiee.fr', '
pbkdf2:sha256:1000000$f9jKuaeciDywyUR6$a358e892b215920e90858d049f64038ad2d8f7a7c20d6a34ff05b1dabdf403b4'),
    ('beatriz.fulgencio', 'beatriz.fulgenciodacunhamenezes@edu.esiee.fr', '
pbkdf2:sha256:1000000$f9jKuaeciDywyUR6$a358e892b215920e90858d049f64038ad2d8f7a7c20d6a34ff05b1dabdf403b4'),
    ('celine.langeland', 'celine.langeland@edu.esiee.fr', '
pbkdf2:sha256:1000000$f9jKuaeciDywyUR6$a358e892b215920e90858d049f64038ad2d8f7a7c20d6a34ff05b1dabdf403b4'),
    ('danick.ngambou', 'danickbaudry.ngambounitcheu@edu.esiee.fr', '
pbkdf2:sha256:1000000$f9jKuaeciDywyUR6$a358e892b215920e90858d049f64038ad2d8f7a7c20d6a34ff05b1dabdf403b4'),
    ('darya.biat', 'darya.biatenia@edu.esiee.fr', '
pbkdf2:sha256:1000000$f9jKuaeciDywyUR6$a358e892b215920e90858d049f64038ad2d8f7a7c20d6a34ff05b1dabdf403b4'),
    ('eric.rajiban', 'eric.rajiban@edu.esiee.fr', '
pbkdf2:sha256:1000000$f9jKuaeciDywyUR6$a358e892b215920e90858d049f64038ad2d8f7a7c20d6a34ff05b1dabdf403b4'),
    ('franck.jiang', 'franck.jiang@edu.esiee.fr', '
pbkdf2:sha256:1000000$f9jKuaeciDywyUR6$a358e892b215920e90858d049f64038ad2d8f7a7c20d6a34ff05b1dabdf403b4'),
    ('jules.bertrand', 'jules.bertrand@edu.esiee.fr', '
pbkdf2:sha256:1000000$f9jKuaeciDywyUR6$a358e892b215920e90858d049f64038ad2d8f7a7c20d6a34ff05b1dabdf403b4'),
    ('julie.johannessen', 'julie.johannessen@edu.esiee.fr', '
pbkdf2:sha256:1000000$f9jKuaeciDywyUR6$a358e892b215920e90858d049f64038ad2d8f7a7c20d6a34ff05b1dabdf403b4'),
    ('julien-aymar.philemy', 'julien-aymar.philemy@edu.esiee.fr', '
pbkdf2:sha256:1000000$f9jKuaeciDywyUR6$a358e892b215920e90858d049f64038ad2d8f7a7c20d6a34ff05b1dabdf403b4'),
    ('muhamed.cengiz', 'muhamed-ali.cengiz@edu.esiee.fr', '
pbkdf2:sha256:1000000$f9jKuaeciDywyUR6$a358e892b215920e90858d049f64038ad2d8f7a7c20d6a34ff05b1dabdf403b4'),
    ('nadine.belinga', 'nadine.belinga@edu.esiee.fr', '
pbkdf2:sha256:1000000$f9jKuaeciDywyUR6$a358e892b215920e90858d049f64038ad2d8f7a7c20d6a34ff05b1dabdf403b4'),
    ('nathan.arnould', 'nathan.arnould@edu.esiee.fr', '
pbkdf2:sha256:1000000$f9jKuaeciDywyUR6$a358e892b215920e90858d049f64038ad2d8f7a7c20d6a34ff05b1dabdf403b4'),
    ('nicolas.charpentier', 'nicolas.charpentier@edu.esiee.fr', '
pbkdf2:sha256:1000000$f9jKuaeciDywyUR6$a358e892b215920e90858d049f64038ad2d8f7a7c20d6a34ff05b1dabdf403b4'),
    ('oceane.bourgeois', 'oceane.bourgeois@edu.esiee.fr', '
pbkdf2:sha256:1000000$f9jKuaeciDywyUR6$a358e892b215920e90858d049f64038ad2d8f7a7c20d6a34ff05b1dabdf403b4'),
    ('paul.saroeun', 'paul.im-saroeun@edu.esiee.fr', '
pbkdf2:sha256:1000000$f9jKuaeciDywyUR6$a358e892b215920e90858d049f64038ad2d8f7a7c20d6a34ff05b1dabdf403b4'),
    ('paul.jurek', 'paul.jurek@edu.esiee.fr', '
pbkdf2:sha256:1000000$f9jKuaeciDywyUR6$a358e892b215920e90858d049f64038ad2d8f7a7c20d6a34ff05b1dabdf403b4'),
    ('ruben.peres', 'ruben.peres@edu.esiee.fr', '
pbkdf2:sha256:1000000$f9jKuaeciDywyUR6$a358e892b215920e90858d049f64038ad2d8f7a7c20d6a34ff05b1dabdf403b4'),
    ('sharumathi.janakiraman', 'sharumathiselvi.janakiraman@edu.esiee.fr', '
pbkdf2:sha256:1000000$f9jKuaeciDywyUR6$a358e892b215920e90858d049f64038ad2d8f7a7c20d6a34ff05b1dabdf403b4'),
    ('yernur.paizkhan', 'yernur.paizkhan@edu.esiee.fr', '
pbkdf2:sha256:1000000$f9jKuaeciDywyUR6$a358e892b215920e90858d049f64038ad2d8f7a7c20d6a34ff05b1dabdf403b4'),
    ('youssef.maghraby', 'youssef.maghraby@edu.esiee.fr', '
pbkdf2:sha256:1000000$f9jKuaeciDywyUR6$a358e892b215920e90858d049f64038ad2d8f7a7c20d6a34ff05b1dabdf403b4');
"""

INSERT_JULIEN = """
INSERT INTO Users (id, username, email, password)
VALUES
    (27, 'julien', 'julien@julien.fr', '
pbkdf2:sha256:1000000$f9jKuaeciDywyUR6$a358e892b215920e90858d049f64038ad2d8f7a7c20d6a34ff05b1dabdf403b4');
"""

INSERT_INTERNSHIPS = """
INSERT INTO Internship (title, company_name, start_date, end_date, application_link, status, user_id)
VALUES
    ('AI Research Intern', 'AI Innovations', '2024-01-15', '2024-06-15', 'https://aiinnovations.com/internship/101', 'Accepted', 27),
    ('Machine Learning Intern', 'DeepLearning Corp', '2024-03-01', '2024-09-01', 'https://deeplearningcorp.com/internship/202', 'Pending', 27),
    ('NLP Intern', 'Language AI', '2024-02-15', '2024-08-15', 'https://languageai.com/internship/303', 'Rejected', 27),
    ('Computer Vision Intern', 'VisionTech', '2024-04-01', '2024-10-01', 'https://visiontech.com/jobs/404', 'Accepted', 27),
    ('AI Systems Intern', 'NextGen AI', '2024-05-01', '2024-11-01', 'https://nextgenai.com/apply/505', 'Pending', 27),
    ('Generative AI Intern', 'GenAI', '2024-06-15', '2024-12-15', 'https://genai.com/internship/606', 'Accepted', 27),
    ('Robotics and AI Intern', 'RoboAI', '2024-07-01', '2024-12-31', 'https://roboai.com/careers/707', 'Rejected', 27),
    ('Software Engineer Intern', 'TechCorp', '2024-01-10', '2024-06-30', 'https://techcorp.com/jobs/123', 'Pending', 1),
    ('Data Analyst Intern', 'DataSolutions', '2024-02-01', '2024-08-01', 'https://datasolutions.com/careers/456', 'Accepted', 2),
    ('Marketing Intern', 'MarketMaven', '2024-03-15', '2024-09-15', 'https://marketmaven.com/jobs/789', 'Rejected', 3),
    ('UI/UX Designer Intern', 'DesignStudio', '2024-04-01', '2024-10-01', 'https://designstudio.com/jobs/101', 'Pending', 4),
    ('Cybersecurity Intern', 'SecureNet', '2024-01-20', '2024-07-20', 'https://securenet.com/internships/202', 'Rejected', 5),
    ('Web Developer Intern', 'CodeFactory', '2024-05-01', '2024-11-01', 'https://codefactory.com/apply/303', 'Accepted', 6),
    ('DevOps Intern', 'CloudOps', '2024-02-15', '2024-08-15', 'https://cloudops.com/jobs/404', 'Pending', 7),
    ('AI Research Intern', 'AI Lab', '2024-06-01', '2024-12-01', 'https://ailab.com/internship/505', 'Rejected', 8),
    ('Product Manager Intern', 'InnoProducts', '2024-03-01', '2024-09-01', 'https://innoproducts.com/jobs/606', 'Accepted', 9),
    ('Embedded Systems Intern', 'ChipTech', '2024-04-15', '2024-10-15', 'https://chiptech.com/careers/707', 'Pending', 10);
"""

# Insérer les données dans la base
with engine.connect() as connection:
    print("Inserting users...")
    connection.execute(text(INSERT_USERS))
    connection.execute(text(INSERT_JULIEN))
    print("Inserting internships...")
    connection.execute(text(INSERT_INTERNSHIPS))
    print("Data insertion complete!")
