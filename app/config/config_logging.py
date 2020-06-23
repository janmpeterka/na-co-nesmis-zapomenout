import logging

# Gunicorn error logger
gunicorn_logger = logging.getLogger("gunicorn.error")
gunicorn_logger.setLevel(logging.WARNING)
