# Steps to create a Django project

1. Create the folder of the project
2. Open a terminal at that folder
3. Create the virtual environment

    - Mac: python3 -m venv venv
    - Windows: python/py -m venv venv

4. Activate the virtual environment

    - Mac: source venv/bin/activate
    - Windows: .\venv\Scripts\activate

5. Install the required dependencies

    - Both OS: pip3 install django

6. Create the django project structure

    - Both OS: django-admin startproject NAME_FOLDER .


7. Create a django app:

    - Both OS: python3 manage.py startapp NAME_OF_THE_APP

8. Run the first migrate command to initialize db:

    - Both OS: python3 manage.py migrate