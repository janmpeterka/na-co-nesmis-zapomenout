import os


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY")

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("DB_STRING")
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://jan:mainframe@localhost:3306/nezapomen"

    # MAIL_SERVER = "smtp.googlemail.com"
    # MAIL_PORT = 465
    # MAIL_USE_TLS = False
    # MAIL_USE_SSL = True
    # MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    # MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    APP_STATE = os.environ.get("APP_STATE")  # production, development, debug, shutdown


class TestConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("TESTING_DB_STRING")
    APP_STATE = os.environ.get(
        "TESTING_APP_STATE"
    )  # production, development, debug, shutdown
    SECRET_KEY = os.environ.get("TESTING_SECRET_KEY")


class DevConfig(Config):
    TEMPLATES_AUTO_RELOAD = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("LOCAL_DB_STRING")
    # SQLALCHEMY_ECHO = True
    APP_STATE = os.environ.get(
        "LOCAL_APP_STATE"
    )  # production, development, debug, shutdown


class ProdConfig(Config):
    pass


configs = {
    "development": DevConfig,
    "test": TestConfig,
    "production": ProdConfig,
    "default": ProdConfig,
}
