from api.models.db import db

class Favourite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_user= db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref='favourite')
    id_recipe= db.Column(db.Integer, db.ForeignKey('recipe.id'))
    recipe = db.relationship('Recipe', backref='favourite')
  
  

    def __repr__(self):
        return '<Favourite %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "id_user": self.id_user,
            "id_recipe": self.id_recipe,
            
            
        }