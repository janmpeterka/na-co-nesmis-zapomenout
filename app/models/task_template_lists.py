from app import db


class TaskTemplateList(db.Model):
    __tablename__ = "task_template_lists"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    description = db.Column(db.Text(), nullable=False)
