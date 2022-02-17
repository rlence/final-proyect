from api.models.index import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post = db.Column(db.String(160), nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref='post')

    def __repr__(self):
        return '<Post %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "post": self.post,
            "user": self.user.serialize()
        } 