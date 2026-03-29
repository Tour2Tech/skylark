0. Git setup:
1. how to setup git and github
2. project => repository setuped in github and clone local system
3. intial prerequisite setup => python version (always choose 2-3 version behind latest) while installing system path always tick
4. VS extension install => python, live server, sqlite viewer


1. Virtual Env:
1. python -m venv .venv => setup the virtual enviornment of python
2. .venv\Scripts\activate

2. Django Setup:
1. create project => django-admin startproject project_name
2. create app => django-admin startapp app_name
3. DB schema creation of project => python manage.py makemigrations
4. DB schema implementation => python manage.py migrate
5. to create admin user => python manage.py createsuperuser
6. to run project => python manage.py runserver

MERN - 
1. MongoDB: Database
2. Express: Server
3. React: Frontend
4. Node.js: Runtime Environment

MEVN - 
1. MongoDB: Database
2. Express: Server
3. Vue.js: Frontend
4. Node.js: Runtime Environment

MEAN - 
1. MongoDB: Database
2. Express: Server
3. Angular: Frontend
4. Node.js: Runtime Environment

28-03-2026

0. project tech stack - django a python based framework, frontend django template (html, css, js)
1. problem statement - crypto/blockchain -- E-Voting System: A tamper-proof platform ensuring each vote is a unique, immutable transaction to prevent election fraud.
2. Points = Monolithic, Microservices, Modular, MVT
3. project structure - 
    - project
    - app
    - templates
    - static
    - manage.py
    - requirements.txt
    - README.md
    - .gitignore
    - .env
    - .env.local
4. directory structure - 
    - crypto_project
        - account
        - admin
        - auth
        - blog
        - contact
        - home
        - services
        - static
        - templates
    - .env
    - manage.py
    - requirements.txt
    - README.md
5. project creation, settings, apps creation with models