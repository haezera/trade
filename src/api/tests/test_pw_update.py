from src.api.server import app
from src.api.tests.clear_db import clear_all

def test_success():
    app.test_client().post('/user/register', json={
        "firstName": "Haeohreum",
        "lastName": "Kim",
        "email": "haeohreum09@hotmail.com",
        "password": "Password123"
    })

    session_id = app.test_client().put('/user/login', json={
        "email": "haeohreum09@hotmail.com",
        "password": "Password123"
    }).json['session_id']

    response = app.test_client().put(f'user/{session_id}/pw/update', json={
        "oldPassword": "Password123",
        "newPassword": "Password1234"
    })
    assert response.status_code == 200
    app.test_client().delete('/clear')


def test_fail():
    app.test_client().post('/user/register', json={
        "firstName": "Haeohreum",
        "lastName": "Kim",
        "email": "haeohreum09@hotmail.com",
        "password": "Password123"
    })

    session_id = app.test_client().put('/user/login', json={
        "email": "haeohreum09@hotmail.com",
        "password": "Password123"
    }).json['session_id']
    
    response = app.test_client().put(f'user/{session_id}/pw/update', json={
        "oldPassword": "Password12345",
        "newPassword": "Password1234"
    })
    assert response.status_code == 200
    app.test_client().delete('/clear')
