CREATE DATABASE IF NOT EXISTS Librairie;
USE Librairie;

CREATE TABLE Client (
    id_client INT PRIMARY KEY AUTO_INCREMENT,
    nom_client VARCHAR(255),
    prenom_client VARCHAR(255),
    email_client VARCHAR(255),
    telephone_client VARCHAR(20),
    preferences_client TEXT,
    adresse_livraison_client TEXT,
    adresse_facturation_client TEXT
);

CREATE TABLE Ouvrage (
    id_ouvrage INT PRIMARY KEY AUTO_INCREMENT,
    titre_ouvrage VARCHAR(255),
    auteur_ouvrage VARCHAR(255),
    isbn_ouvrage VARCHAR(20),
    langue_ouvrage VARCHAR(20),
    prix_ouvrage DECIMAL(10, 2),
    date_parution_ouvrage DATE,
    categorie_ouvrage VARCHAR(255),
    date_disponibilite_libraire_ouvrage DATE,
    date_disponibilite_particulier_ouvrage DATE,
    image_ouvrage VARCHAR(255),
    table_des_matieres_ouvrage TEXT,
    mot_cle_ouvrage TEXT,
    description_ouvrage TEXT
);

CREATE TABLE Theme (
    id_theme INT PRIMARY KEY AUTO_INCREMENT,
    nom_theme VARCHAR(255)
);

CREATE TABLE Theme_Ouvrage (
    id_ouvrage INT,
    id_theme INT,
    PRIMARY KEY (id_ouvrage, id_theme),
    FOREIGN KEY (id_ouvrage) REFERENCES Ouvrage(id_ouvrage),
    FOREIGN KEY (id_theme) REFERENCES Theme(id_theme)
);

CREATE TABLE Commentaire (
    id_commentaire INT PRIMARY KEY AUTO_INCREMENT,
    id_client INT,
    id_ouvrage INT,
    date_publication_commentaire DATE,
    auteur_commentaire VARCHAR(255),
    titre_commentaire VARCHAR(255),
    FOREIGN KEY (id_client) REFERENCES Client(id_client),
    FOREIGN KEY (id_ouvrage) REFERENCES Ouvrage(id_ouvrage)
);