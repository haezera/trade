from src.api.server import app
from src.api.tests.clear_db import clear_all
from src.api.tests.test_user_login import create_user


def test_email_update_success():
    create_user()
    session_id = app.test_client().put('/user/login', json={
        "email": "haeohreum09@hotmail.com",
        "password": "Password123"
    }).json["session_id"]
    response = app.test_client().put(f"/user/{session_id}/email/update", json={
        "newEmail": "haeohreum04@gmail.com",
        "password": "Password123"
    })
    assert response.status_code == 200
    clear_all()

def test_email_update_fail():
    \
