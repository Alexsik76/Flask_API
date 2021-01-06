from dateutil.parser import parse
from datetime import datetime
import os


def get_report() -> list:
    needed_files = ('abbreviations.txt', 'start.log', 'end.log')
    """Creates a time-sorted list of drivers with all the necessary data.

    :return: A sorted by time list of dicts.
    :rtype: list[tuple[]]
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
        :rtype: tuple[str, str, str,datetime, datetime, timedelta]
        """
        titles, s_start, s_finish = line
        start = parse(s_start, fuzzy=True)
        finish = parse(s_finish, fuzzy=True)
        race_time = datetime.min + abs(finish - start)
        abr, name, team = titles.split('_')
        return (abr,
                name,
                team,
                start.time(),
                finish.time(),
                race_time.time())

    source_racers = zip(*[read_file(file_name) for file_name in needed_files])
    racers = sorted([parsing_line(line) for line in source_racers], key=lambda x: x[5])
    print(racers)
    return racers
