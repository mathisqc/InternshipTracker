-- Supprimer la base de données si elle existe
DROP DATABASE IF EXISTS internships_db;

-- Créer une nouvelle base de données
CREATE DATABASE internships_db;

-- Se connecter à la nouvelle base
\c internships_db;

-- Créer la table Users
CREATE TABLE IF NOT EXISTS Users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(80) NOT NULL UNIQUE,
    email VARCHAR(120) NOT NULL UNIQUE,
    password VARCHAR(128) NOT NULL
);

-- Créer la table Internship
CREATE TABLE IF NOT EXISTS Internship (
    id SERIAL PRIMARY KEY,
    title VARCHAR(120) NOT NULL,
    company_name VARCHAR(120) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    application_link VARCHAR(255) NOT NULL,
    status VARCHAR(50) NOT NULL,
    user_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE CASCADE
);

-- Insérer les utilisateurs avec le mot de passe

INSERT INTO Users (username, email, password)
VALUES
    ('alexandre.saiphou', 'alexandre.saiphou@edu.esiee.fr', '
1234
'),
    ('alexis.simon', 'alexis.simon@edu.esiee.fr', '
1234
'),
    ('alseny.yoro', 'alseny.yoro@edu.esiee.fr', '
1234
'),
    ('antoine.dolley', 'antoine.dolley@edu.esiee.fr', '
1234
'),
    ('antoine.merlet', 'antoine.merlet@edu.esiee.fr', '
1234
'),
    ('beatriz.fulgencio', 'beatriz.fulgenciodacunhamenezes@edu.esiee.fr', '
1234
'),
    ('celine.langeland', 'celine.langeland@edu.esiee.fr', '
1234
'),
    ('danick.ngambou', 'danickbaudry.ngambounitcheu@edu.esiee.fr', '
1234
'),
    ('darya.biat', 'darya.biatenia@edu.esiee.fr', '
1234
'),
    ('eric.rajiban', 'eric.rajiban@edu.esiee.fr', '
1234
'),
    ('franck.jiang', 'franck.jiang@edu.esiee.fr', '
1234
'),
    ('jules.bertrand', 'jules.bertrand@edu.esiee.fr', '
1234
'),
    ('julie.johannessen', 'julie.johannessen@edu.esiee.fr', '
1234
'),
    ('julien-aymar.philemy', 'julien-aymar.philemy@edu.esiee.fr', '
1234
'),
    ('muhamed.cengiz', 'muhamed-ali.cengiz@edu.esiee.fr', '
1234
'),
    ('nadine.belinga', 'nadine.belinga@edu.esiee.fr', '
1234
'),
    ('nathan.arnould', 'nathan.arnould@edu.esiee.fr', '
1234
'),
    ('nicolas.charpentier', 'nicolas.charpentier@edu.esiee.fr', '
1234
'),
    ('oceane.bourgeois', 'oceane.bourgeois@edu.esiee.fr', '
1234
'),
    ('paul.saroeun', 'paul.im-saroeun@edu.esiee.fr', '
1234
'),
    ('paul.jurek', 'paul.jurek@edu.esiee.fr', '
1234
'),
    ('ruben.peres', 'ruben.peres@edu.esiee.fr', '
1234
'),
    ('sharumathi.janakiraman', 'sharumathiselvi.janakiraman@edu.esiee.fr', '
1234
'),
    ('yernur.paizkhan', 'yernur.paizkhan@edu.esiee.fr', '
1234
'),
    ('youssef.maghraby', 'youssef.maghraby@edu.esiee.fr', '
1234
');

-- Insérer l'utilisateur 'julien' en dernier avec un ID explicite
INSERT INTO Users (id, username, email, password)
VALUES
    (27, 'julien', 'julien@julien.fr', '
1234
');

-- Insérer les stages après avoir ajouté 'julien'
INSERT INTO Internship (title, company_name, start_date, end_date, application_link, status, user_id)
VALUES
    ('AI Research Intern', 'AI Innovations', '2024-01-15', '2024-06-15', 'https://aiinnovations.com/internship/101', 'Accepted', 27),
    ('Machine Learning Intern', 'DeepLearning Corp', '2024-03-01', '2024-09-01', 'https://deeplearningcorp.com/internship/202', 'Pending', 27),
    ('NLP Intern', 'Language AI', '2024-02-15', '2024-08-15', 'https://languageai.com/internship/303', 'Rejected', 27),
    ('Computer Vision Intern', 'VisionTech', '2024-04-01', '2024-10-01', 'https://visiontech.com/jobs/404', 'Accepted', 27),
    ('AI Systems Intern', 'NextGen AI', '2024-05-01', '2024-11-01', 'https://nextgenai.com/apply/505', 'Pending', 27),
    ('Generative AI Intern', 'GenAI', '2024-06-15', '2024-12-15', 'https://genai.com/internship/606', 'Accepted', 27),
    ('Robotics and AI Intern', 'RoboAI', '2024-07-01', '2024-12-31', 'https://roboai.com/careers/707', 'Rejected', 27);


-- Insérer des stages fictifs associés aux utilisateurs
INSERT INTO Internship (title, company_name, start_date, end_date, application_link, status, user_id)
VALUES
    -- Stages pour les autres utilisateurs
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