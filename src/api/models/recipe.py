from api.models.db import db

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    photo = db.Column(db.String(200), unique=False, nullable=True)
    title = db.Column(db.String(80), unique=False, nullable=False)
    description = db.Column(db.String(1000), unique=True, nullable=False)
    private = db.Column(db.Boolean, default=False)
    tag = db.Column(db.Integer)
    id_user= db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref='recipe')
  

    def __repr__(self):
        return '<Recipe %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "photo": self.photo,
            "title": self.title,
            "description": self.description,
            "private": self.private,
            "tag": self.tag,
            "id_user": self.id_user,
            
        }