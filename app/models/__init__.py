# This is needed for Flask-Migrate to work
# import all tables that are not classes (only raw M:N relationship tables)
# imports automatically (because it's __init__.py file)

from .request_log import RequestLog  # noqa: F401

# This is needed for ExtendedFlaskView to automatically import all Model classes
from .notifications import Notification  # noqa: F401
# from .sent_mails import SentMails  # noqa: F401
from .task_lists import TaskList  # noqa: F401
from .task_template_lists import TaskTemplateList  # noqa: F401
from .task_templates import TaskTemplate  # noqa: F401
from .tasks import Task  # noqa: F401
from .users import User  # noqa: F401

