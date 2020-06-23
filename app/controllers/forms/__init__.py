# This is needed for ExtendedFlaskView to automatically import all Form classes

from .login import LoginForm  # noqa: F401
from .password_recovery import NewPasswordForm  # noqa: F401
from .password_recovery import GetNewPasswordForm  # noqa: F401
from .register import RegisterForm  # noqa: F401
