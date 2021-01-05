from app import create_app, db_wrapper
from app.models import Racer, from_files_to_db

app = create_app()

if not db_wrapper.database.get_tables():
    with db_wrapper.database as db:
        db.create_tables([Racer])
        from_files_to_db()


@app.shell_context_processor
def make_shell_context():
    return {'db': db_wrapper.database, 'Racer': Racer}
