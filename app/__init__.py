from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


mail = Mail()
db = SQLAlchemy()
migrate = Migrate()

# WIP - necessary before anything from models is imported elswhere
import app.models


def create_app(config_name="default"):
    application = Flask(__name__, instance_relative_config=True)

    # CONFIG
    from config import configs

    application.config.from_object(configs[config_name])

    # TODO - not loading from config for some reason
    application.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "mysql+pymysql://jan:mainframe@localhost:3306/nezapomen"

    # APPS
    mail.init_app(application)
    db.init_app(application)
    migrate.init_app(application, db)

    # LOGGING
    # from .config.config_logging import db_handler, gunicorn_logger

    # application.logger.addHandler(gunicorn_logger)
    # application.logger.addHandler(db_handler)

    # CONTROLLERS
    from .controllers import register_all_controllers  # noqa: F401

    register_all_controllers(application)

    from .controllers import register_error_handlers  # noqa: F401

    register_error_handlers(application)

    # MODULES

    return application
