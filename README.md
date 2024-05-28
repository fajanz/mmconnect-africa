Choice of Technology Stack and Alignment with Project Requirements.
Python (Django).
Why Django: Django is a powerful Python framework that simplifies web development with built-in features like an ORM, authentication, and URL routing.
Project Fit: It allows for rapid development and clean, maintainable code, which is ideal for creating a robust application for MMConnect Africa.

MySQL Database.
Why MySQL: MySQL is a reliable and scalable relational database system.
Project Fit: It efficiently handles data storage and retrieval, meeting the project's need for managing records effectively.

HTML/CSS/JavaScript
Why HTML/CSS/JavaScript: These are essential web technologies for structuring, styling, and adding interactivity to web pages.
Project Fit: They ensure the web application has a user-friendly and visually appealing interface, making it easy for users to add and view records.

To set up and run the MMConnect Africa web application on another computer, follow these detailed steps:

Prerequisites
Python 3.8 or higher
MySQL Server

Set Up MySQL Database: 
Install MySQL Server:-

Download and install MySQL from the official website: https://dev.mysql.com/downloads/
Create a Database "mmconnect_db".

Configure the Django Project to Use MySQL by running cmd and writting command:-
-python manage.py makemigrations
-python manage.py migrate

Run the project:
- python manage.py runserver

copy this link and paste to the browser to run the system:
http://127.0.0.1:8000/records/

