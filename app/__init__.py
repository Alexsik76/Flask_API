from flask import Flask
from config import app_config, create_swag_config
from flask_bootstrap import Bootstrap
from flask_restful import Api
from flasgger import Swagger

from flaskext.markdown import Markdown
from playhouse.flask_utils import FlaskDB


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
    db_wrapper.init_app(app)
    dtb = db_wrapper.database
    from app.models import Racer
    with dtb:
        Racer.create_table()
        with app.app_context():
            Racer.init_db()
        for racer in Racer.select():
            racer.race_time = racer.get_race_time()
        for number, racer in enumerate(Racer.select().order_by(Racer.race_time), start=1):
            racer.position = number
            print(racer.name, racer.start, racer.finish, racer.position, sep='=>')
    bootstrap.init_app(app)
    from app.api import bp as api_bp
    from app.api.api_report import ApiReport

    my_api.add_resource(ApiReport, '/api/v1/report/')
    my_api.init_app(api_bp)

    app.register_blueprint(api_bp)

    from app.main import bp
    app.register_blueprint(bp)

    Markdown(app)
    app.config['SWAGGER'] = create_swag_config()
    swag.init_app(app)
    return app
