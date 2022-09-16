from app.system.extensions import db


class Repository(object):

    def __init__(self, object=None):
        self.object = object
        self.db = db

    def save(self):
        self.db.session.add(self.object)
        self.db.session.commit()

    def delete_object(self):
        self.db.session.delete(self.object)
        self.db.session.commit()

    def find(self, object_id):
        obj = self.object.query.filter_by(id=object_id).first()
        return obj
