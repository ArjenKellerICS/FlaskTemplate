# imports
import os
from typing import List, Type

# # when auto scheduling tasks
# from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore

basedir = os.path.abspath(os.path.dirname(__file__))
APPLICATION_NAME = "FlaskTemplate"


# Base config class for inheritance
class BaseConfig:
    CONFIG_NAME = "base"
    # flask base settings
    USE_MOCK_EQUIVALENCY = False
    DEBUG = False
    # Flask settings
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = None

    # # scheduler settings
    # JOBS = [
    #     {
    #         'id': 'sync_job: 1',
    #         'func': 'app.service_scheduler:sync_job_1',
    #         'trigger': 'cron',
    #         'second': 59
    #     }
    # ]
    # SCHEDULER_JOBSTORES = {
    #     "default": SQLAlchemyJobStore(url=f"sqlite:///{basedir}/ap-scheduler.db")
    # }
    # SCHEDULER_API_ENABLED = True
    # security
    JWT_SECRET_KEY = "ThisIsATest"


class DevelopmentConfig(BaseConfig):
    CONFIG_NAME = "dev"

    # flask settings
    SECRET_KEY = os.getenv("DEV_SECRET_KEY", "PythonIsBeterDanVisualBah-Sick")
    DEBUG = True

    # sql-alchemy settings
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir}/{APPLICATION_NAME}-Dev.db"

    #  other
    TESTING = False


class TestingConfig(BaseConfig):
    CONFIG_NAME = "test"

    # flask settings
    SECRET_KEY = os.getenv("TEST_SECRET_KEY", "Thanos did nothing wrong")
    DEBUG = True

    # sql-alchemy settings
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir}/{APPLICATION_NAME}-Test.db"

    # other
    TESTING = True


class ProductionConfig(BaseConfig):
    CONFIG_NAME = "prod"

    # flask settings
    SECRET_KEY = os.getenv("PROD_SECRET_KEY", "ICSPythonSuperDevs")
    DEBUG = False

    # sql-alchemy settings
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir}/{APPLICATION_NAME}-Prod.db"

    # other
    TESTING = False


EXPORT_CONFIGS: List[Type[BaseConfig]] = [
    DevelopmentConfig,
    TestingConfig,
    ProductionConfig
]

config_by_name = {cfg.CONFIG_NAME: cfg for cfg in EXPORT_CONFIGS}


