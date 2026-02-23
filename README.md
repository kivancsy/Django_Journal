Journal App
A personal journaling web application built with Django. Users can register, log in, and manage their own journal entries.
Features

User registration and authentication (Django built-in auth)
Create, read, update, and delete journal entries
Each user can only see and manage their own entries
Django template-based frontend

Installation

Clone the repository

bash   git clone https://github.com/kullanicin/journal-app.git
   cd journal-app

Create a virtual environment

bash   python -m venv venv
   source venv/bin/activate

Install dependencies

bash   pip install -r requirements.txt

Set up environment variables

bash   cp .env.example .env
Then edit .env and add your own SECRET_KEY.

Run migrations

bash   python manage.py migrate

Start the server

bash   python manage.py runserver

Visit http://127.0.0.1:8000 in your browser.