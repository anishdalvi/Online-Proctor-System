# Online-Proctor-System
A system that enables the proctor to easily manage the information about a particular student and access it easily

1. Clone this Project
2. Create a virtual environment <br>

    `pip install -r requirements.txt`
2. Configure database information in the settings.py file of the project folder(proctor)
3. Then, <br>

    `python manage.py makemigrations` <br>

    `python manage.py migrate` <br>

    `python manage.py runserver`