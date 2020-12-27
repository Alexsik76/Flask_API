from peewee import *
import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    db = SqliteDatabase(':memory:')
    if 'db' not in g:
        g.db = db
    return g.db


def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()


def init_db():
    with current_app.app_context():
        for racer in current_app.extensions['table'].report:
            Racer.create(abr=racer['Abbreviation'],
                         name=racer['Name'],
                         team=racer['Team'],
                         start=racer['Start time'],
                         finish=racer['Finish time'],
                         race_time=racer['Race time'],
                         position=racer['Position'])


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


class Racer(Model):
    abr = FixedCharField(max_length=3)
    name = CharField()
    team = CharField()
    start = TimeField(formats='%H:%M:%S.%f')
    finish = TimeField(formats='%H:%M:%S.%f')
    race_time = TimestampField(resolution=3, utc=True)
    position = IntegerField()

    class Meta:
        with current_app.app_context():
            database = get_db()
