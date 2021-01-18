from app import create_app, db_wrapper
from app.models import Racer

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {'db': db_wrapper.database, 'Racer': Racer}
