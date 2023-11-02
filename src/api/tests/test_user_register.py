from src.api.server import app
from src.api.tests.clear_db import clear_all


def test_register_success():
    response = app.test_client().post('/user/register', json={
        "firstName": "Haeohreum",
        "lastName": "Kim",
        "email": "haeohreum09@hotmail.com",
        "password": "Password123"
    })
    res = response.status_code
    assert res == 200
    clear_all()


def test_register_fail_name():
    response = app.test_client().post('/user/register', json={
        "firstName": "",
        "lastName": "Kim",
        "email": "haeohreum09@hotmail.com",
        "password": "Password123"
    })
    res = response.status_code
    assert res == 400
    clear_all()


def test_register_fail_email():
    response = app.test_client().post('/user/register', json={
        "firstName": "Haeohreum",
        "lastName": "Kim",
        "email": "",
        "password": "Password123"
    })
    res = response.status_code
    assert res == 400
    clear_all()


def test_register_fail_password():
    response = app.test_client().post('/user/register', json={
        "firstName": "Haeohreum",
        "lastName": "Kim",
        "email": "haeohreum09@hotmail.com",
        "password": ""
    })
    res = response.status_code
    assert res == 400
    clear_all()

