from src.api.server import app
<<<<<<< HEAD
import src.api.tests.test_user_login as login
from src.api.tests.clear_db import clear_all


def tests_incomestmt_success():
=======
from src.api.tests.clear_db import clear_all
import src.api.tests.test_user_login as login


def test_awsm_success():
>>>>>>> 7cfb28bf4b2ac62715c3be3083e66aa3fdd237f0
    login.create_user()
    session_id = app.test_client().put('/user/login', json={
        "email": "haeohreum09@hotmail.com",
        "password": "Password123"
    }).json["session_id"]
    ticker = "AAPL"
    response = app.test_client().get(
<<<<<<< HEAD
        f"/stock/{session_id}/{ticker}/awsm",
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
        f"/stock/{session_id}/{ticker}/awsm",
        query_string={
            "startDate": "2020-01-01",
            "endDate": "2020-01-10"
        })
    assert response.status_code == 400
    clear_all()
=======
        f"/stock/{session_id}/{ticker}/awsm/2023-01-10/2023-01-20")

    assert response.status_code == 200
    clear_all()
>>>>>>> 7cfb28bf4b2ac62715c3be3083e66aa3fdd237f0
