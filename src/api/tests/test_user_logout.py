from src.api.server import app
import src.api.tests.test_user_login as login
from src.api.tests.clear_db import clear_all


# Test success case
def test_user_logout_success():
    login.create_user()
    session_id = app.test_client().put('/user/login', json={
        "email": "haeohreum09@hotmail.com",
        "password": "Password123"
    }).json["session_id"]
    response = app.test_client().put('/user/logout', json={
        "sessionId": session_id
    })
    clear_all()
    assert response.status_code == 200
