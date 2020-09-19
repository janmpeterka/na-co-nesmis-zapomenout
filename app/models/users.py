from flask_security import UserMixin

from app import db


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    # pwdhash = db.Column(db.CHAR(64), nullable=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)

    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    @staticmethod
    def load(user_identifier, load_type="id"):
        if load_type == "id":
            user = db.session.query(User).filter(User.id == user_identifier).first()
        elif load_type == "username":
            user = (
                db.session.query(User).filter(User.username == user_identifier).first()
            )
        elif load_type == "google_id":
            user = (
                db.session.query(User).filter(User.google_id == user_identifier).first()
            )
        elif load_type == "new_password_token":
            user = (
                db.session.query(User)
                .filter(User.new_password_token == user_identifier)
                .first()
            )
        else:
            return None

        return user
