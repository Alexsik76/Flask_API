# This option does not use classes and uses a minimum of functions.
# Therefore, many Comprehensions are used.
from datetime import datetime
from dateutil.parser import parse
import os
from flask import current_app


class Table:
    def __init__(self, app=None):
        self.report = []
        self.path = None
        if app is not None:
            self.init_app(app)

    def init_app(self, app) -> None:
        """Initialize this class with the given :class:`flask.Flask` instance.

                :param app: the Flask application or blueprint object
                :type app: flask.Flask

                Examples::
                    table.init_app(app)
        """
        with app.app_context():
            self.path = self.get_path()
            self.report = self.get_report() if self.path else []
        if not hasattr(app, 'extensions'):
            app.extensions = {}
        app.extensions['table'] = self

    def read_file(self, file_name: str) -> list:
        """Reading any file and returning sorted by text list of strings.

        :param file_name: A files` name.
        :type file_name: str
        :return: Sorted list of strings.
        :rtype: list
        """

        path_to_file = os.path.join(self.path, file_name)
        with open(path_to_file, encoding='utf8') as file:
            sorted_file = sorted([line.strip() for line in file if line.strip()])
        return sorted_file

    @staticmethod
    def parsing_line(line: tuple) -> tuple:
        """Divides the line to data.

        :param line: A line combined with three tapes of input files.
        :type line: tuple
        :return: A list of data.
        :rtype: tuple[str, str, str, datetime, datetime, datetime]
        """
        titles, s_start, s_finish = line
        abr, name, team = titles.split('_')
        start = parse(s_start, fuzzy=True)
        finish = parse(s_finish, fuzzy=True)
        race_time = datetime.min + abs(finish - start)
        return (abr,
                name,
                team,
                start.time(),
                finish.time(),
                race_time.time())

    def get_report(self) -> list:
        """Creates a time-sorted list of drivers with all the necessary data.

        :return: A sorted by time list of dicts.
        :rtype: list[dict]
        """
        source_racers = zip(*[self.read_file(file_name) for file_name in current_app.config.get('FILE_NAMES')])
        racers = [dict(zip(current_app.config.get('FIELDS'), (None, *self.parsing_line(line))))
                  for line in source_racers]
        racers.sort(key=lambda x: x['Race time'])
        for number, racer in enumerate(racers, start=1):
            racer['Position'] = number
            racer['Start time'] = racer['Start time'].isoformat(timespec="milliseconds")
            racer['Finish time'] = racer['Finish time'].isoformat(timespec="milliseconds")
            racer['Race time'] = racer['Race time'].isoformat(timespec="milliseconds")
        return racers

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
