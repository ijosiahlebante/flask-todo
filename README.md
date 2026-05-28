# Flask Todo App - REST API Enhancement

## Original Application

This project is a simple Flask Todo application using SQLite and SQLAlchemy.

## Added Feature

I added a Categories REST API feature with full CRUD functionality.

## API Endpoints

### Get All Categories

GET /api/categories

### Get Single Category

GET /api/categories/<id>

### Create Category

POST /api/categories

### Update Category

PUT /api/categories/<id>

### Delete Category

DELETE /api/categories/<id>

## Technologies Used

* Flask
* Flask-SQLAlchemy
* SQLite
* Pytest
* Postman

## Testing

Unit tests were created using pytest to verify:

* Create Category
* Read Categories
* Update Category
* Delete Category
* Error handling

## How to Run

Install dependencies:

pip install flask==2.2.5
pip install flask-sqlalchemy==2.5.1
pip install sqlalchemy==1.4.46
pip install werkzeug==2.2.3
pip install pytest

Run the application:

python app.py

Run tests:

pytest
