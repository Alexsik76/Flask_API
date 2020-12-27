from peewee import *
import click
from flask import current_app, g
from flask.cli import with_appcontext
from app import Racer
from playhouse.sqlite_ext import *


# def get_db():
#     if 'db' not in g:
#         g.db = db
#     return g.db
#
#
# def close_db(e=None):
#     db = g.pop('db', None)
#     if db is not None:
#         db.close()


def init_db(app, dtb):
    # print(dir(db_wrapper))
    # with db_wrapper.database:
    #     print(db_wrapper.database)
    for racer in app.extensions['table'].report:
        # print(dir(app.Racer))
        print(dtb.is_closed())
        print(dtb.obj.__doc__)
        Racer.create(position=racer['Position'],
                     abr=racer['Abbreviation'],
                     name=racer['Name'],
                     team=racer['Team'],
                     start=racer['Start time'],
                     finish=racer['Finish time'],
                     race_time=racer['Race time'])

# @click.command('init-db')
# @with_appcontext
# def init_db_command():
#     """Clear the existing data and create new tables."""
#     init_db()
#     click.echo('Initialized the database.')
#
#
# def init_app(app):
#     app.teardown_appcontext(close_db)
#     app.cli.add_command(init_db_command)
