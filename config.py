from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'dev'
    STATIC_FOLDER = 'app/static'
    TEMPLATES_FOLDER = 'app/templates'
    JSON_SORT_KEYS = False
    FILE_NAMES = ('abbreviations.txt', 'start.log', 'end.log')
    FIELDS = ('Position', 'Abbreviation', 'Name', 'Team', 'Start time', 'Finish time', 'Race time')
    BOOTSTRAP_BOOTSWATCH_THEME = 'cosmo'


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


app_config = {
    'base_config': Config,
    'testing': TestingConfig,
    'develop': DevelopmentConfig
}