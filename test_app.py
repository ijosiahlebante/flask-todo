import json
from app import app, db, Category


app.config['TESTING'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

client = app.test_client()


def setup_module(module):
    with app.app_context():
        db.create_all()


def teardown_module(module):
    with app.app_context():
        db.drop_all()


def test_create_category():

    response = client.post(
        '/api/categories',
        json={
            'name': 'School'
        }
    )

    assert response.status_code == 201


def test_get_categories():

    response = client.get('/api/categories')

    assert response.status_code == 200


def test_get_single_category():

    response = client.get('/api/categories/1')

    assert response.status_code == 200


def test_update_category():

    response = client.put(
        '/api/categories/1',
        json={
            'name': 'Updated'
        }
    )

    assert response.status_code == 200


def test_delete_category():

    response = client.delete('/api/categories/1')

    assert response.status_code == 200


def test_category_not_found():

    response = client.get('/api/categories/999')

    assert response.status_code == 404


def test_create_category_without_name():

    response = client.post(
        '/api/categories',
        json={}
    )

    assert response.status_code == 400