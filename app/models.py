from peewee import *
from app.read_files import get_report
from app import db_wrapper


class ShortTimeField(Field):
    field_type = 'short_time'

    def db_value(self, value):
        if value.microsecond/1000 == int(value.microsecond/1000):
            return value.time().isoformat(timespec="milliseconds")
        else:
            return value.time()


class Racer(db_wrapper.Model):
    abr = CharField()
    name = CharField()
    team = CharField()
    start = ShortTimeField()
    finish = ShortTimeField()
    race_time = ShortTimeField()

    def __repr__(self):
        return f'<Racer {self.id, self.abr, self.name, self.race_time}>'


def init_models():
    if not Racer.table_exists():
        print('table_exists 2 => ', Racer.table_exists())
        with db_wrapper.database.atomic():
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
