from src.api.server import app
import src.api.tests.test_user_login as login
from src.api.tests.clear_db import clear_all


def test_vwap_success():
    login.create_user()
    session_id = app.test_client().put('/user/login', json={
        "email": "haeohreum09@hotmail.com",
        "password": "Password123"
    }).json["session_id"]
    ticker = "AAPL"
    response = app.test_client().get(
        f"/stock/{session_id}/{ticker}/vwap",
        query_string={
            "startDate": "2020-01-01",
            "endDate": "2020-01-10"
        })

    assert response.status_code == 200
    clear_all()


def tests_incomestmt_fail_ticker():
    login.create_user()
    session_id = app.test_client().put('/user/login', json={
        "email": "haeohreum09@hotmail.com",
        "password": "Password123"
    }).json["session_id"]
    ticker = "AASDSADSADSADSA"
    response = app.test_client().get(
        f"/stock/{session_id}/{ticker}/vwap",
        query_string={
            "startDate": "2020-01-01",
            "endDate": "2020-01-10"
        })
    assert response.status_code == 400
    clear_all()
