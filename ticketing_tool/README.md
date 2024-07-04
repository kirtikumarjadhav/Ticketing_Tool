## PROJECT STRUCTURE
ticketing_tool/
├── manage.py
├── ticketing_tool/
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│ └── asgi.py
├── tickets/
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── forms.py
│ ├── models.py
│ ├── tests.py
│ ├── urls.py
│ └── views.py
├── static/
│ ├── css/
│ │ ├── base.css
│ │ ├── login.css
│ │ └── signup.css
│ └── images/
├── templates/
│ ├── base_generic.html
│ ├── index.html
│ ├── login.html
│ ├── signup.html
│ └── tickets/
│ ├── create_ticket.html
│ └── ticket_list.html
└── requirements.txt

## Create a virtual environment and activate it

`venv\Scripts\activate`

## Install the dependencies

pip install -r requirements.txt

## Apply migrations

python manage.py migrate

## python manage.py createsuperuser

python manage.py createsuperuser

## Run the development server

python manage.py runserver

## Static Files

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]


## PROJECT STURCTURE

Project Structure Description
    - manage.py: A command-line utility that lets you interact with this Django project.

ticketing_tool/: The main project directory.
    -init.py: An empty file that tells Python that this directory should be considered a Python package.
    -settings.py: Contains all the settings and configurations for your Django project.
    -urls.py: The URL declarations for this Django project.
    -wsgi.py: An entry-point for WSGI-compatible web servers to serve your project.
    -asgi.py: An entry-point for ASGI-compatible web servers to serve your project.

tickets/: The app directory.
    -init.py: An empty file that tells Python that this directory should be considered a Python package.
    -admin.py: Used to register models to be managed through the Django admin interface.
    -apps.py: Contains the configuration for the app.
    -forms.py: Contains forms for the app.
    -models.py: Contains models for the app.
    -tests.py: Contains tests for the app.
    -urls.py: The URL declarations for this app.
    -views.py: Contains views for the app.

static/: The directory for static files.
    -css/: Contains CSS files.
        -base.css: Base CSS file.
        -login.css: CSS for the login page.
        -signup.css: CSS for the signup page.

templates/: The directory for templates.
  - base_generic.html: The base template.
  - index.html: The homepage template.
  - login.html: The login page template.
  - signup.html: The signup page template.
  - tickets/: The directory for ticket-related templates.
  - create_ticket.html: The create ticket page template.
  - ticket_list.html: The ticket list page template.
  
requirements.txt: A file that lists all the dependencies for your project


