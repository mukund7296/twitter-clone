# Twitter Clone

A simplified social media application with user profiles and post functionality.

![Screenshot](screenshot.png) <!-- Add actual screenshot later -->

## Features

- User registration and authentication
- Profile management (bio, location, professional info)
- Create and view posts (280 character limit)
- Responsive UI with Bootstrap
- Admin dashboard

## Technologies

- Django 5.2
- Bootstrap 5
- SQLite
- Django Crispy Forms
- Pillow (Image handling)

## Setup Instructions

### 1. Project setup 
```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
````
```bash
# Install Django
pip install django

# Create project and app
django-admin startproject twitter_clone
cd twitter_clone
````
```bash
python manage.py startapp core
````

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```bash
SECRET_KEY=your-secret-key-here
DEBUG=True
```

You can generate a secret key using:

```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

### 5. Apply Migrations

```bash
python manage.py migrate
```

### 6. Create a Superuser (Admin)

```bash
python manage.py createsuperuser
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

Open your browser and visit: [http://localhost:8000](http://localhost:8000)

---

## 🔐 Test Credentials

| Username   | Password      |
| ---------- | ------------- |
| `testuser` | `testpass123` |

---

## 📁 Project Structure

```
twitter-clone/
├── core/                 # Main Django app
│   ├── migrations/       # DB migrations
│   ├── templates/        # HTML templates
│   ├── admin.py          # Admin configuration
│   ├── models.py         # Database models
│   └── views.py          # App logic
├── twitter_clone/        # Project settings
│   ├── settings.py       # Settings and configs
│   └── urls.py           # URL routing
├── .env                  # Environment variables
├── requirements.txt      # Python dependencies
└── manage.py             # Django CLI
```

---

## 🔑 Admin Access

Visit: [http://localhost:8000/admin](http://localhost:8000/admin)

Use the superuser credentials created in Step 6.

---
