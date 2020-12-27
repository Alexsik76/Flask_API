from datetime import datetime
from dateutil.parser import parse
import os
from flask import current_app
from peewee import *
from app import db_wrapper



class Racer(db_wrapper.Model):
    position = IntegerField(null=True)
    abr = CharField()
    name = CharField()
    team = CharField()
    start = DateTimeField()
    finish = DateTimeField()
    race_time = TimeField(null=True)

    def get_race_time(self):
        time = abs(self.finish - self.start)
        return time

    @classmethod
    def init_db(cls):
        for racer in cls.get_report():
            Racer.create(abr=racer['Abbreviation'],
                         name=racer['Name'],
                         team=racer['Team'],
                         start=racer['Start time'],
                         finish=racer['Finish time'])

    @staticmethod
    def get_path() -> str:
        """
        Finds and returns a path to the files positioning.

        :return: path to the files positioning.
        :rtype: str
        """
        places = os.walk(os.path.abspath(os.path.join(__file__, "../..")))
        needed_files = current_app.config.get('FILE_NAMES')

        def condition(files):
            return all(file in files for file in needed_files)

        return next((path for path, dirs, files in places if condition(files)), None)

    @classmethod
    def read_file(cls, file_name: str) -> list:
        """Reading any file and returning sorted by text list of strings.

        :param file_name: A files` name.
        :type file_name: str
        :return: Sorted list of strings.
        :rtype: list
        """

        path_to_file = os.path.join(cls.get_path(), file_name)
        with open(path_to_file, encoding='utf8') as file:
            sorted_file = sorted([line.strip() for line in file if line.strip()])
        return sorted_file

    @staticmethod
    def parsing_line(line: tuple) -> tuple:
        """Divides the line to data.

        :param line: A line combined with three tapes of input files.
        :type line: tuple
        :return: A list of data.
        :rtype: tuple[str, str, str, str, str]
        """
        print(line)
        titles, start, finish = line
        abr, name, team = titles.split('_')
        return (abr,
                name,
                team,
                parse(start, fuzzy=True),
                parse(finish, fuzzy=True))

    @classmethod
    def get_report(cls) -> list:
        """Creates a time-sorted list of drivers with all the necessary data.

        :return: A sorted by time list of dicts.
        :rtype: list[dict]
        """
        source_racers = zip(*[cls.read_file(file_name) for file_name in current_app.config.get('FILE_NAMES')])
        racers = [dict(zip(current_app.config.get('FIELDS'), (None, *cls.parsing_line(line))))
                  for line in source_racers]
        return racers
