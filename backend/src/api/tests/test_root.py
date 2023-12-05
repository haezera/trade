from src.api.server import app


def test_root_one():
    response = app.test_client().get('/')
    res = response.json
    assert res == {"message": "You accessed the root!"}
