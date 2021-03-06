from flask import Flask
from config import app_config
from flask_bootstrap import Bootstrap
from flask_restful import Api
from flasgger import Swagger
from playhouse.flask_utils import FlaskDB
from flaskext.markdown import Markdown

bootstrap = Bootstrap()
my_api = Api()
swag = Swagger()
db_wrapper = FlaskDB()


def create_app(test_config=None):
    app = Flask(__name__)
    if test_config:
        app.config.from_object(app_config['testing'])
    else:
        app.config.from_object(app_config['develop'])

    bootstrap.init_app(app)
    from app.api import bp as api_bp
    from app.api.api_report import ApiReport

    my_api.add_resource(ApiReport, '/api/v1/report/')
    my_api.init_app(api_bp)

    app.register_blueprint(api_bp)

    from app.main import bp
    app.register_blueprint(bp)

    swag.init_app(app)

    db_wrapper.init_app(app)
    from app import db
    db.init_app(app)

    Markdown(app, output_format='html4')
    print("App is created")
    return app
