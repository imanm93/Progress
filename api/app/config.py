import os
from .common.constants import INSTANCE_FOLDER_PATH

class BaseConfig(object):

    PROJECT = "app"
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

    ENV = 'development'
    DEBUG = False
    TESTING = False

    ADMINS = ["iman.m93@gmail.com"]

    # TODO: Implement more secure secret key
    SECRET_KEY = "secret_key"


class DefaultConfig(BaseConfig):

    # Debug environment
    DEBUG = True

    # Connection to Localhost
    DB_URI = "mongodb://localhost:27017/"

    SECRET_KEY = "development_key"


class DevConfig(DefaultConfig):
    """ Development Configuration """
    DB_URI = "mongodb://db:27017/"
    GRAPHDB_URI = "http://localhost:7474/db/data"


class StagingConfig(DefaultConfig):
    """ Staging Configuration """
    pass


class ProdConfig(DefaultConfig):
    """ Production Configuration """
    pass


def get_config(MODE):
    SWITCH = {
        'DEV'     : DevConfig,
        'STAGING' : StagingConfig,
        'PROD'    : ProdConfig
    }
    return SWITCH[MODE]
