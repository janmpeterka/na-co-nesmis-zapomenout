from app import db


class TaskTemplate(db.Model):
    __tablename__ = "task_templates"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    task_template_list_id = db.Column(db.ForeignKey("task_template_lists.id"), nullable=False)

    description = db.Column(db.Text(), nullable=False)
