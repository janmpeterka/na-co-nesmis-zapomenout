from app import db


class Notification(db.Model):
    __tablename__ = "notifications"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    sent_at = db.Column(db.DateTime, nullable=True)

    task_id = db.Column(db.ForeignKey("tasks.id"), nullable=False)
