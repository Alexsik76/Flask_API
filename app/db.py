import click
from flask.cli import with_appcontext

from app import db_wrapper
from app.models import Racer
from app.read_files import get_report


def init_db():
    db = db_wrapper.database
    if Racer.table_exists():
        Racer.drop_table()
    with db.atomic():
        Racer.create_table()
        data = get_report()
        Racer.insert_many(data, fields=[Racer.abr,
                                        Racer.name,
                                        Racer.team,
                                        Racer.start,
                                        Racer.finish,
                                        Racer.race_time]
                          ).execute()

        print('Data stored to the DB')


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    # app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
