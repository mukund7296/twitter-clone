# Twitter Clone

A simplified social media application with user profiles and post functionality.

<img width="1433" alt="image" src="https://github.com/user-attachments/assets/c3bb8d23-fbe3-4350-88a5-5e67e7eaf8ff" />


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
<img width="749" alt="image" src="https://github.com/user-attachments/assets/f1729948-9e72-4fb6-b385-e1cd0b462492" />


### 2. Configure Settings
Add to twitter_clone/settings.py:

```bash
INSTALLED_APPS = [
    ...
    'core.apps.CoreConfig',
    'crispy_forms',
    'crispy_bootstrap5',
]


STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Add this line
STATICFILES_DIRS = [BASE_DIR / 'static']  # Create 'static' directory if needed

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'core.User'

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

LOGIN_REDIRECT_URL = 'home'
LOGIN_URL = 'login'
```

### 3. Install Dependencies
add to requirements.txt
```bash
asgiref==3.8.1
crispy-bootstrap5==2025.4
Django==5.2.1
django-crispy-forms==2.4
pillow==11.2.1
sqlparse==0.5.3
```
To install all module in virtual environment area follow below command 
```bash
pip install -r requirements.txt
```

### 4. update all files from repository to your System fresh files(copy - Paste) 

```bash
update twitter-clone/urls.py (copy - Paste) 
update core/forms.py (Manually create forms.py file) & (copy - Paste) ) - for registration
update core/urls.py (Manually create urls.py file) & (copy - Paste) )
update core/admin.py  (copy - Paste) - to display all modules at Admin Panel UI/UX (to See all models this step required)
update core/views.py  (copy - Paste)- Here is the main logic
update core/admin.py  (copy - Paste)
update core/models.py  (copy - Paste) - Here are the all Models or Database tables
update core/admin.py  (copy - Paste)

# Create HTML templates folder 
Create core/templates/core/base.html - (create manually file & copy - Paste content)
Create other templates (home.html, profile.html, register.html, login.html, logout.html) following similar structure and (copy paste ).
```

<img width="309" alt="image" src="https://github.com/user-attachments/assets/03786ddc-cff8-4214-b9f4-6e49d87430a2" />

### 5. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a Superuser (Admin)

```bash
python manage.py createsuperuser
```
This user : admin  & password :******(Need to set here)

### 7. Run the Development Server

```bash
python manage.py runserver
```
<img width="1031" alt="image" src="https://github.com/user-attachments/assets/cd757af3-01ac-4326-9009-6551a4024c97" />

### Open your browser and visit: [http://127.0.0.1:8081/](http://127.0.0.1:8081/)

## Main Page 

<img width="1431" alt="image" src="https://github.com/user-attachments/assets/54c03004-cad8-47de-9326-66b862f3a3a5" />

## Registration Page 
http://127.0.0.1:8081/register/
<img width="1422" alt="image" src="https://github.com/user-attachments/assets/0bb9e484-efd8-486c-881f-4cc1090ec5fe" />

## Login Page 
http://127.0.0.1:8081/login/
<img width="1428" alt="image" src="https://github.com/user-attachments/assets/3fd98ab8-3c12-41f8-82a6-b04b9a2baae4" />

## Profile page 

http://127.0.0.1:8081/profile/
<img width="1429" alt="image" src="https://github.com/user-attachments/assets/56522dc0-c3cc-4a1f-8a01-8613e7de96f6" />


## Main posts Page
<img width="1433" alt="image" src="https://github.com/user-attachments/assets/b26d9d55-96af-4f92-84d1-652d3170cd71" />

##  Admin Access

Visit: [http://127.0.0.1:8081/admin](http://127.0.0.1:8081/admin)


<img width="1238" alt="image" src="https://github.com/user-attachments/assets/8cab98af-5298-48b5-8309-374371ea9660" />

## Here Admin can see all Modules User , Pofiles and Posts. 
<img width="1440" alt="image" src="https://github.com/user-attachments/assets/6060b452-1b00-468c-af3a-9e12228dcb70" />

## All posts and filter to filter posts based on user 
<img width="1435" alt="image" src="https://github.com/user-attachments/assets/fa67939a-0af3-482c-9cfb-f093915714a7" />

---

## Thank you
