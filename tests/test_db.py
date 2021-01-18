from app.models import Racer


def test_db(client):
    assert Racer.table_exists()
    team = Racer.select().where(Racer.team == 'FERRARI')
    assert len(team) == 2


def test_hello(runner):
    result = runner.invoke(args=['init-db'])
    assert 'Initialized the database.' in result.output
