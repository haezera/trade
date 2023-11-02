from src.api.server import app
from src.api.tests.clear_db import clear_all
import src.api.tests.test_user_login as login


def test_awsm_success():
    login.create_user()
    session_id = app.test_client().put('/user/login', json={
        "email": "haeohreum09@hotmail.com",
        "password": "Password123"
    }).json["session_id"]
    ticker = "AAPL"
    response = app.test_client().get(
        f"/stock/{session_id}/{ticker}/awsm/2023-01-10/2023-01-20")

    assert response.status_code == 200
    clear_all()
