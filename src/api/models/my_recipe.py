from api.models.db import db

class MyRecipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.Integer)
    id_user= db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref='user_myrecipe')
    id_recipe= db.Column(db.Integer, db.ForeignKey('recipe.id'))
    recipe = db.relationship('Recipe')
  
  

    def __repr__(self):
        return '<MyRecipe %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user": self.user.serialize(),
            "recipe": self.recipe.serialize()
            
            
        }