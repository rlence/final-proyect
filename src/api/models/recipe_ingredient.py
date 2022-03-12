from api.models.db import db

class Recipe_ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer)
    id_ingredient= db.Column(db.Integer, db.ForeignKey('ingredient.id'))
    id_recipe= db.Column(db.Integer, db.ForeignKey('recipe.id'))
  
    # ingredient = db.relationship('Ingredient')
    # recipe = db.relationship('Recipe')

  

    def __repr__(self):
        return '<Recipe_ingredient %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "quantity": self.quantity,
            "id_ingredient": self.id_ingredient,
            "id_recipe": self.id_recipe,
            
            
        }