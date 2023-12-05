from src.api.server import app 


def clear_all():
    app.test_client().delete('/clear')
