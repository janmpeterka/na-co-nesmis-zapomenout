import datetime

from app import db

from app.models.base_mixin import BaseMixin


class SentMail(db.Model, BaseMixin):
    __tablename__ = "sent_mails"

    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    subject = db.Column(db.String(255), nullable=False)
    sender = db.Column(db.String(255), nullable=False)
    recipient_id = db.Column(db.ForeignKey(("users.id")), nullable=False, index=True)
    bcc = db.Column(db.String(255), nullable=True)
    template = db.Column(db.Text(), nullable=True)

    created_at = db.Column(db.DateTime, nullable=True, default=datetime.datetime.now)

    recipient = db.relationship("User", uselist=False, back_populates="sent_mails")

    def fill_from_message(self, message):
        self.subject = message.subject
        self.sender = message.sender
        self.recipient_id = message.recipient.id
        self.bcc = ", ".join(message.bcc)
        self.template = getattr(message, "template", None)
