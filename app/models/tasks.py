from app import db


class Task(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    task_list_id = db.Column(db.ForeignKey("task_lists.id"), nullable=False, index=True)
    task_template_id = db.Column(db.ForeignKey("task_templates.id"), nullable=False)

    description = db.Column(db.Text(), nullable=False)
