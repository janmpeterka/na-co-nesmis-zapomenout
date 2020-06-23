from flask import Blueprint
from flask import redirect, flash, url_for, session
from flask import current_app as application

from flask_login import login_user, logout_user, current_user, login_required

# from flask_dance.contrib.google import google
# from flask_dance.consumer import oauth_authorized

from app.models.users import User


auth_blueprint = Blueprint("auth", __name__, template_folder="templates/auth/")


# @oauth_authorized.connect
# def oauth_login(blueprint, token):
#     # TODO: rewrite for multiple oaths @TEST (30)
#     if blueprint.name == "google":
#         try:
#             user_info = google.get("/oauth2/v2/userinfo").json()
#             # username = user_info["email"]
#             google_id = user_info["id"]
#         except Exception as e:
#             application.logger.error(e)
#     else:
#         # not implemented
#         return False

#     if blueprint.name == "google":
#         user = User.load(google_id, load_type="google_id")

#     if user:
#         do_oauth_login(user=user, oauth_type="google")
#     else:
#         do_oauth_register(user_info=user_info, oauth_type="google")


# def do_oauth_register(*, user_info, oauth_type):
#     user = User()
#     user.username = user_info["email"]
#     user.password = None
#     user.google_id = user_info["id"]

#     if "given_name" in user_info:
#         user.first_name = user_info["given_name"]
#     else:
#         user.first_name = "-"

#     if "family_name" in user_info:
#         user.last_name = user_info["family_name"]
#     else:
#         user.last_name = "-"

#     do_register(user, source="google_oauth")


# def do_oauth_login(*, user, oauth_type=None):
#     if oauth_type == "google":
#         if user.google_id is not None:
#             login_user(user)
#             return True


def do_login(username=None, password=None, from_register=False):
    if not isinstance(password, bytes) and password is not None:
        password = password.encode("utf-8")

    user = User.load(username, load_type="username")

    if user is not None and user.check_login(password):
        login_user(user, remember=True)
        user.log_login()

        if from_register:
            flash(
                "Byl jste úspěšně zaregistrován. Protože jste v aplikaci nově, může vám pomoci <a href={}>Nápověda</a>".format(
                    url_for("SupportView:help")
                ),
                "success",
            )
        return True
    else:
        flash("Přihlášení se nezdařilo.", "error")
        return False


@login_required
@auth_blueprint.route("/logout")
def do_logout():
    session.pop("logged_from_admin", None)
    if current_user.is_authenticated:
        logout_user()
    return redirect(url_for("LoginView:show"))


def do_register(user, source=None):
    if user.save() is True:
        # if source == "google_oauth":
        # do_oauth_login(user=user, oauth_type="google")
        # else:
        do_login(
            username=user.username,
            password=user.password.encode("utf-8"),
            from_register=True,
        )
        return True
    else:
        flash("Registrace neproběhla v pořádku", "error")
        return False


def validate_register(username):
    """
    Tests for registration validity:
        - unique username

    Arguments:
        username {string}
    Returns:
        bool
    """
    if User.load(username, load_type="username") is not None:
        return False
    else:
        return True


def generate_new_password_token(user):
    import secrets

    token = secrets.token_hex(40)
    set_new_password_token(user, token)
    return token


def set_new_password_token(user, token):
    user.new_password_token = token
    user.edit()
    return True
