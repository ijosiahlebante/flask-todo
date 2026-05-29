# Flask Todo App REST API Enhancement

## Original Application

This project is based on the Flask Todo App created by Patrick Loeber. The application allows users to create, complete, and delete todo tasks using Flask, SQLite, and SQLAlchemy.

## Enhancement Added

I added a Categories REST API feature to extend the functionality of the application.

The Categories API supports full CRUD operations:

* Create Category
* Read Categories
* Update Category
* Delete Category

## API Endpoints

### Create Category

POST /api/categories

### Get All Categories

GET /api/categories

### Get Single Category

GET /api/categories/<id>

### Update Category

PUT /api/categories/<id>

### Delete Category

DELETE /api/categories/<id>

## Features Implemented

* RESTful API design
* JSON request and response handling
* Proper HTTP status codes
* Error handling for invalid or missing resources
* Automated testing using pytest

## Technologies Used

* Flask
* Flask-SQLAlchemy
* SQLite
* Postman
* Pytest

## Testing

Automated tests were created to verify:

* Create operations
* Read operations
* Update operations
* Delete operations
* Error handling and negative test cases

## How to Run

1. Activate the virtual environment.
2. Run:

python app.py

3. Open:

http://127.0.0.1:5000

## Run Tests

pytest
