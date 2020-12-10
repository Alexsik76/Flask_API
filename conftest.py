import pytest
from app import create_app


@pytest.fixture(scope='session')
def app():
    app = create_app(test_config=True)
    return app


# @pytest.fixture
# def client(app):
#     with app.test_client() as client:
#         yield client
#
#
# @pytest.fixture
# def runner(app):
#     return app.test_cli_runner()
