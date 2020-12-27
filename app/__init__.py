from flask import Flask
from config import app_config, create_swag_config
from flask_bootstrap import Bootstrap
from flask_restful import Api
from flasgger import Swagger
from app.models import RaceTable
from flaskext.markdown import Markdown
from peewee import *
from playhouse.flask_utils import FlaskDB

bootstrap = Bootstrap()
my_api = Api()
table = RaceTable()
swag = Swagger()
db_wrapper = FlaskDB()


class Racer(db_wrapper.Model):
    position = IntegerField()
    abr = CharField()
    name = CharField()
    team = CharField()
    start = TimeField(formats='%H:%M:%S.%f')
    finish = TimeField(formats='%H:%M:%S.%f')
    race_time = TimestampField(resolution=3, null=True)

    def get_race_time(self):
        self.race_time = self.finish - self.start

def create_app(test_config=None):
    app = Flask(__name__)
    if test_config:
        app.config.from_object(app_config['testing'])
    else:
        app.config.from_object(app_config['develop'])
    table.init_app(app)
    db_wrapper.init_app(app)
    dtb = db_wrapper.database
    with dtb:
        print('DB is closed: ', dtb.is_closed())
        Racer.create_table()
        print(Racer.table_exists())
        racer = table.report[0]
        print(racer['Race time'], type(racer['Race time']))
        Racer.create(abr=racer['Abbreviation'],
                     position=racer['Position'],
                     name=racer['Name'],
                     team=racer['Team'],
                     start=racer['Start time'],
                     finish=racer['Finish time'])
        print(dtb.select().columns())
    #     from app import db
    #     db.init_db(app, dtb)
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
