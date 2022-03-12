from api.models.db import db

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_user= db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref='user_comment')
    id_recipe= db.Column(db.Integer, db.ForeignKey('recipe.id'))
    recipe = db.relationship('Recipe', backref='recipe_comment')
  
  

    def __repr__(self):
        return '<Comment %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "id_user": self.id_user,
            "id_recipe": self.id_recipe,
            
            
        }