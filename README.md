# Data Representation Project

## Project Description

Create a project that demonstrates that the student understands the course information and can implement the materials learned during the Data Representataion module of the Data & Analytics course.

## Description
The project involves creating a web application in Flask that has a restful API. The App links to the datarepresentation database. A webpage (index.html) is created that consumes the API and performs CRUD (Create, Update, Delete) operations using ajax calls on the data.

## Project steps
- Create Virtual Environment (venv)
- Create App Server using Flask (server.py)
- Run App server
- Implement and Test CRUD operations using CURL on browser
- Write the code for each function
- Create database and database table using sql. Crate a copy of table in python (initdb.sql)
- Write code for the DAO. (dpDAO.py). DAO connects the database, gets and retriewes data to/from the server
- Test the DAO to ensure it works correctly (testDogDAO.py)
- Create the webpage interface (index.html). Write the code that connects it to the database and performs all the CRUD operations and updates database.


### Files included in the project:

- .gitignore
- initDB
- Requirements.txt
- Server.py
- dogDAO.py
- testDogDAO.py
- staticpages/index.html
- staticpages/dogs.jpeg
- README.MD
- venv