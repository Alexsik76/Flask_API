from app import create_app, db_wrapper
from app.models import Racer, from_files_to_db

app = create_app()

with app.app_context():
    if not db_wrapper.database.get_tables():
        from_files_to_db()


@app.shell_context_processor
def make_shell_context():
    return {'db': db_wrapper.database, 'Racer': Racer}
