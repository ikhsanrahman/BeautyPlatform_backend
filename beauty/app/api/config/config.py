"""
    Configuration
    _______________
    This is module for storing all configuration for various environments
"""
import os
import arrow


basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """ This is base class for configuration """
    SECRET_KEY = os.getenv('SECRET_KEY', '!@#$%^&*()?><)(*&GHJK$%')
    DEBUG = False
  
    DATABASE = {
        "DRIVER"   : os.getenv('DB_DRIVER')     or "postgresql", # sqlite // postgresql // mysql
        "USERNAME" : os.getenv('DB_USERNAME')   or "beauty",
        "PASSWORD" : os.getenv('DB_PASSWORD')   or "beauty",
        "HOST_NAME": os.getenv('DB_HOSTNAME')   or "localhost",
        "DB_NAME"  : os.getenv('DB_NAME')       or "db_beauty",
    }

    VIDEO_FOLDER = 'data/video'
    FILE_FOLDER = 'data/file'

    def time() :
        utc         = arrow.utcnow()
        local       = utc.to('Asia/Jakarta')
        time        = local.isoformat()
        return time
#end class


class DevelopmentConfig(Config):
    """ This is class for development configuration """
    DEBUG = True
    DATABASE = Config.DATABASE
    VIDEO_FOLDER = Config.VIDEO_FOLDER
    FILE_FOLDER = Config.FILE_FOLDER
    SQLALCHEMY_DATABASE_URI = DATABASE["DRIVER"] + "://" + DATABASE["USERNAME"] + ":" + \
                                DATABASE["PASSWORD"] + "@" + DATABASE["HOST_NAME"] + "/" + \
                                DATABASE["DB_NAME"] + "_dev"
    print(SQLALCHEMY_DATABASE_URI)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

#end class


class TestingConfig(Config):
    """ This is class for testing configuration """
    DEBUG = True
    TESTING = True

    VIDEO_FOLDER = Config.VIDEO_FOLDER
    FILE_FOLDER = Config.FILE_FOLDER

    DATABASE = Config.DATABASE
    SQLALCHEMY_DATABASE_URI = DATABASE["DRIVER"] + "://" + DATABASE["USERNAME"] + ":" + \
                                DATABASE["PASSWORD"] + "@" + DATABASE["HOST_NAME"] + "/" + \
                                DATABASE["DB_NAME"] + "_test"
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

#end class


class ProductionConfig(Config):
    """ This is class for production configuration """
    DEBUG = True

    VIDEO_FOLDER = Config.VIDEO_FOLDER
    FILE_FOLDER = Config.FILE_FOLDER

    DATABASE = Config.DATABASE
    SQLALCHEMY_DATABASE_URI = DATABASE["DRIVER"] + "://" + DATABASE["USERNAME"] + ":" + \
                                DATABASE["PASSWORD"] + "@" + DATABASE["HOST_NAME"] + "/" + \
                                DATABASE["DB_NAME"] + "_prod"
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

#end class


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
