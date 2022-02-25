from api.models.db import db

class Rol(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rol_name = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return '<Rol %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "rol_name": self.rol_name,
        }