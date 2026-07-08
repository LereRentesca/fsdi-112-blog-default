# Class #2 - Django Template Language + Jinja and Static Files

## Overview:

    Introduction to DTL and recap of some Jinja tags. DTL is the syntax used by Django’s built-in template engine to separate presentation logic from Python backend code.  It allows developers to embed dynamic content into HTML, XML, or other text-based formats without writing executable Python code within the templates.

## Strucure of the class:

- Start the class with some QA or fixing bugs from previous class.
- Ask for Assignment #1 and then do the solution of the assignment.
- Recap of Class 1:
    - Explain the structure of the project (purpose of each folder)
    - Explain why the pages app was created (Django works with applications, it help us to organize and distribute the logic of our project. Just with the basic structure we're not able to display something we need apps to contain our logic)
    - Explain how HomePageView was created and how it connects with home.html
- Introduction of DTL with the creation of the base.html, navbar.html and start implementing those changes onto existing htmls (home and about)
    - Add bootstrap to base so they can use it on the rest of htmls
- Introduction of static files (how to load css, js and images on htmls)
- Do the example with the home.html and give them some time to adjust the other htmls.

## If you need extra topics

- Show them the admin page and help them creating a the superuser from the terminal
    - Step 1: Open a terminal on the desired folder and activate the venv
    - Step 2: Run the command "python manage.py createsuperuser"
    - Step 3: The terminal will prompt you to enter: username, email, password (I always tell them to call it admin and the same for the password)
    - Step 4: The terminal will prompt you if you want to bypass and type the letter "y", then hit enter
    - Step 5: Run the server "python manage.py runserver" and go to localhost:8000/admin
    - Step 6: Log in as admin and show the system

## Additional notes

1. **{% extends 'file.html' %}** | This tag allow us to get the content from another html (in this case our base.html)
2. **{% load static %}** | This tag allow us to load any css, js or images onto that file
3. **{% block NAME %}{% endblock %}** | This tag allow us to create spaces to work on the base.html
4. **{% include 'file.html' %}** | This tag allow us to insert code at the level where we place it. 