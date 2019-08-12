import os
import logging

from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from logstash_async.handler import LogstashFormatter
import logstash

from . import config as Config
from .common import constants as COMMON_CONSTANTS
from .api import schools, universities

# For import
__all__ = ['create_app']

# For Swagger UI
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Progress"
    }
)

DEFAULT_BLUEPRINTS = [
    schools,
    universities
]

def create_app(config=None, app_name=None, blueprints=None):
    """ Create a Flask app """

    if app_name is None:
        app_name = Config.DefaultConfig.PROJECT

    if blueprints is None:
        blueprints = DEFAULT_BLUEPRINTS

    app = Flask(app_name, instance_path=COMMON_CONSTANTS.INSTANCE_FOLDER_PATH, instance_relative_config=True)
    configure_app(app, config)
    configure_hook(app)
    configure_blueprints(app, blueprints)
    configure_extensions(app)
    configure_logging(app)
    configure_error_handlers(app)

    return app


def configure_app(app, config=None):
    """ Configure app for dev/prod/staging """

    app.config.from_object(Config.DefaultConfig)

    if config:
        app.config.from_object(config)
        return

    application_mode = os.getenv('APPLICATION_MODE', 'DEV')
    app.config.from_object(Config.get_config(application_mode))


def configure_extensions(app):
    # Init DB
    pass


def configure_blueprints(app, blueprints):
    # Register blueprints
    for blueprint in blueprints:
        app.register_blueprint(blueprint)

    # Register Swagger UI
    app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)


def configure_logging(app):

    app.logger = logging.getLogger("python-logstash-logger")
    app.logger.setLevel(logging.DEBUG)

    logstash_host = os.environ.get('LOGSTASH_HOST')

    handler = logstash.TCPLogstashHandler(logstash_host, 5959, version=1)
    formatter = LogstashFormatter()
    handler.setFormatter(formatter)

    app.logger.addHandler(handler)
    app.logger.info('Logging setup complete')


def configure_hook(app):
    @app.before_request
    def before_request():
        pass


def configure_error_handlers(app):

    @app.errorhandler(404)
    def not_found_page(error):
        return "404 - Page not found"

    @app.errorhandler(500)
    def server_error_page(error):
        return "500 - Internal server error"
