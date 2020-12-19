from os import path
from dotenv import load_dotenv
from flask import current_app
from jinja2 import Template, Environment, BaseLoader, FileSystemLoader



basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


def create_swag_config(app):
    # boots = app.jinja_env.globals['bootstrap']
    # print(boots)
    # with app.app_context():
    #     head_text = Environment(loader=FileSystemLoader('app/templates')).get_template('head.html').render(globals(), bootstrap=boots)
    #     top_text = Environment(loader=FileSystemLoader('app/templates')).get_template('navbar.html').render()
    #     footer_text = Environment(loader=FileSystemLoader('app/templates')).get_template('footer.html').render()
    s_config = {'title': 'REST API report of Monaco 2018 Racing',
                'uiversion': 3,
                'openapi': '3.0.2',
                'version': '0.0.3',
                'hide_top_bar': True
                # 'footer_text': footer_text,
                # 'top_text': 'bootstrap.load_css()',
                # 'head_text': 'bootstrap.load_css()',
                }
    return s_config


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
    # BOOTSTRAP_ICON_SIZE = '1.5em'
    # BOOTSTRAP_ICON_COLOR = 'light'






class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True


class TestingConfig(Config):
    DEBUG = False
    TESTING = True


app_config = {
    'base_config': Config,
    'testing': TestingConfig,
    'develop': DevelopmentConfig
}
