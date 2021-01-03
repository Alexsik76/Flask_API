from dateutil.parser import parse
import os
from peewee import *
from app import db_wrapper


class Racer(db_wrapper.Model):
    position = IntegerField(null=True)
    abr = CharField(unique=True)
    name = CharField()
    team = CharField()
    start = DateTimeField()
    finish = DateTimeField()
    race_time = TimeField(null=True)

    def get_race_time(self):
        time = abs(self.finish - self.start)
        return time

    def __repr__(self):
        return f'<Racer {self.position, self.abr, self.name, self.race_time}>'


def init_db():
    Racer.create_table()
    for racer in get_report():
        Racer.create(abr=racer['Abbreviation'],
                     name=racer['Name'],
                     team=racer['Team'],
                     start=racer['Start time'],
                     finish=racer['Finish time'])


def get_report() -> list:
    needed_files = ('abbreviations.txt', 'start.log', 'end.log')
    fields = ('Position', 'Abbreviation', 'Name', 'Team', 'Start time', 'Finish time', 'Race time')
    """Creates a time-sorted list of drivers with all the necessary data.

    :return: A sorted by time list of dicts.
    :rtype: list[dict]
    """

    def get_path() -> str:
        """
        Finds and returns a path to the files positioning.

        :return: path to the files positioning.
        :rtype: str
        """
        places = os.walk(os.path.abspath(os.path.join(__file__, "../..")))

        def condition(files):
            return all(file in files for file in needed_files)

        return next((path for path, dirs, files in places if condition(files)), None)

    def read_file(file_name: str) -> list:
        """Reading any file and returning sorted by text list of strings.

        :param file_name: A files` name.
        :type file_name: str
        :return: Sorted list of strings.
        :rtype: list
        """

        path_to_file = os.path.join(get_path(), file_name)
        with open(path_to_file, encoding='utf8') as file:
            sorted_file = sorted([line.strip() for line in file if line.strip()])
        return sorted_file

    def parsing_line(line: tuple) -> tuple:
        """Divides the line to data.

        :param line: A line combined with three tapes of input files.
        :type line: tuple
        :return: A list of data.
        :rtype: tuple[str, str, str, str, str]
        """
        titles, start, finish = line
        abr, name, team = titles.split('_')
        return (abr,
                name,
                team,
                parse(start, fuzzy=True),
                parse(finish, fuzzy=True))
    source_racers = zip(*[read_file(file_name) for file_name in needed_files])
    racers = [dict(zip(fields, (None, *parsing_line(line))))
              for line in source_racers]
    return racers


def from_files_to_db():

    init_db()

    for racer in Racer.select():
        racer.race_time = racer.get_race_time()
        racer.save()
    for number, racer in enumerate(Racer.select().order_by(Racer.race_time), start=1):
        racer.position = number
        racer.save()
    print('Data stored to the DB')
