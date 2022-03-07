from api.models.db import db

class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False, nullable=False)
    create_at = db.Column(db.Date)
    id_user= db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref='menu')
  

    def __repr__(self):
        return '<Menu %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "create_at": self.create,
            "id_user": self.id_user,
            
        }