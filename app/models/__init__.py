# This is needed for Flask-Migrate to work
# import all tables that are not classes (only raw M:N relationship tables)
# imports automatically (because it's __init__.py file)

from .request_log import RequestLog  # noqa: F401

# This is needed for ExtendedFlaskView to automatically import all Model classes
from .users import User  # noqa: F401
