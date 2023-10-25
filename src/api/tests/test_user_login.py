from src.api.server import app
from src.api.tests.clear_db import clear_all


def create_user():
    app.test_client().post('/user/register', json={
        "firstName": "Haeohreum",
        "lastName": "Kim",
        "email": "haeohreum09@hotmail.com",
        "password": "Password123"
    })


def test_login_success():
    create_user()
    response = app.test_client().put('/user/login', json={
        "email": "haeohreum09@hotmail.com",
        "password": "Password123"
    })
    assert response.status_code == 200
    clear_all()


def test_login_fail_pw():
    create_user()
    response = app.test_client().put('/user/login', json={
        "email": "haeohreum09@hotmail.com",
        "password": "Password1234"
    })
    assert response.status_code == 400
    clear_all()


def test_login_fail_email():
    create_user()
    response = app.test_client().put('/user/login', json={
        "email": "haeohreum04@gmail.com",
        "password": "Password123"
    })
    assert response.status_code == 400
    clear_all()
