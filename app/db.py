from peewee import *
import click
from flask import current_app, g
from flask.cli import with_appcontext
from app.models import Racer
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



        # rc.get_race_time()
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
