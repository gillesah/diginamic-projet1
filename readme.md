
# Test API python sqlalchemy

## Description

Ce projet de creation d'une API a été réalisé dans le cadre de notre formation en tant que developpeur fullstack chez Diginamic. Il s'agit d'une application développée en Python 3.11, utilisant plusieurs librairies et frameworks pour différentes fonctionnalités.

## Fonctionnalités

- L'application utilise le framework FastAPI pour créer une API performante.
- Elle se connecte à une base de données mariaSQL à l'aide de la librairie pyMySQL.
- La gestion de l'ORM est assurée par la librairie SqlAlchelmy.
- Les tests unitaires sont mis en place avec le module unittest.
- Le serveur d'application est démarré à l'aide de la librairie Uvicorn.

## Architecture du Projet

Le projet suit une structure standard pour un projet Python. Voici un aperçu :

```
diginamic-project1/
    |- README.md
    |- requirements.txt
    |- main.py
    |- .gitignore
    |- __init__.py
	|- src
		|- models/
			|- __init__.py
			|- ...
		|- router/
			|- __init__.py
			|- ...
		|- schema/
			|- __init__.py
			|- ...
		|- docs/
			|- ...
    |- tests/
        |- __init__.py
        |- ...
    |- config/
        |- __init__.py
        |- connexion.py
        |- ...

```

- Le dossier `projet/` contient le code source de l'application, avec ses différents modules.
- Les tests unitaires sont placés dans le dossier `tests/`.
- Les fichiers de documentation et les cahiers de charge se trouvent dans le dossier `docs/`.

## Installation

1. Clonez ce dépôt sur votre machine locale.
2. Assurez-vous d'avoir **Python 3.11** installé sur votre système.
3. Créez un environnement virtuel et activez-le.
4. À l'intérieur de l'environnement virtuel, exécutez la commande suivante pour installer les dépendances du projet :
   ```bash
   pip install -r requirements.txt
   ```

## Utilisation

1. Assurez-vous que votre environnement virtuel est activé.
2. Accédez au répertoire du projet.
3. Exécutez la commande suivante pour démarrer le serveur d'application :
   ```bash
   uvicorn main:app --reload
   ```
   Cela lancera le serveur d'application sur `http://localhost:8000`.

## Contributions

Ce projet a été développé par [Gilles Helleu](https://github.com/gillesah), [Guillaume Lemaitre](https://github.com/glem1) et [Benjamin Hadjaz](https://github.com/0bshidian). [Kanban sur Github](src/docs/image.png)

## Commandes

Ajouter une dépendance au projet :

```bash
pip freeze > requirements.txt
```
