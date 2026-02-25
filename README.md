# Journal App

A personal journaling web application built with Django. Users can register, log in, and manage their own journal entries.

🔗 **Live:** https://djangojournal-production.up.railway.app/

## Features

- User registration and authentication (Django built-in auth)
- Create, read, update, and delete journal entries
- Each user can only see and manage their own entries
- Django template-based frontend
- PostgreSQL database
- Dockerized

## Running Locally

### With Docker (recommended)

1. Clone the repository
   ```bash
   git clone https://github.com/kivancsy/Django_Journal.git
   cd Django_Journal
   ```

2. Set up environment variables
   ```bash
   cp .env.example .env
   ```
   Then edit `.env` and fill in your values.

3. Start with Docker Compose
   ```bash
   docker-compose up --build
   ```

4. Visit `http://127.0.0.1:8000` in your browser.

### Without Docker

1. Clone the repository
   ```bash
   git clone https://github.com/kivancsy/Django_Journal.git
   cd Django_Journal
   ```

2. Create a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables
   ```bash
   cp .env.example .env
   ```
   Then edit `.env` and fill in your values.

5. Run migrations
   ```bash
   python manage.py migrate
   ```

6. Start the server
   ```bash
   python manage.py runserver
   ```

7. Visit `http://127.0.0.1:8000` in your browser.