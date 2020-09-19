from flask import current_app as application

from sqlalchemy.exc import DatabaseError

from app import db


# Custom methods for all my classes
class BaseMixin(object):
    @classmethod
    def load(cls, *args, **kwargs):
        if "id" in kwargs:
            cls_id = kwargs["id"]
        else:
            cls_id = args[0]
        my_object = db.session.query(cls).filter(cls.id == cls_id).first()
        return my_object

    @classmethod
    def load_all(cls):
        my_objects = db.session.query(cls)
        return my_objects

    def update(self, **kw):
        try:
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            application.logger.error("Edit error: {}".format(e))
            return False

    def create(self, **kw):
        """Saves (new) object
        """
        try:
            db.session.add(self)
            db.session.commit()
            if self.id is not None:
                return True
            else:
                return False
        except DatabaseError as e:
            db.session.rollback()
            application.logger.error("Save error: {}".format(e))
            return False

    def delete(self, **kw):
        """Deletes object
        """
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except DatabaseError as e:
            db.session.rollback()
            application.logger.error("Remove error: {}".format(e))
            return False

    # def expire(self, **kw):
    #     """Dumps database changes
    #     """
    #     try:
    #         db.session.expire(self)
    #         return True
    #     except Exception as e:
    #         db.session.rollback()
    #         application.logger.error("Expire error: {}".format(e))
    #         return False

    # def refresh(self, **kw):
    #     try:
    #         db.session.refresh(self)
    #         return True
    #     except Exception as e:
    #         db.session.rollback()
    #         application.logger.error("Refresh error: {}".format(e))
    #         return False
