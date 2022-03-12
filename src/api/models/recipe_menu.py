from api.models.db import db

class Recipe_menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_menu= db.Column(db.Integer, db.ForeignKey('menu.id'))
    menu = db.relationship('Menu', backref='menu_in_recipe_menu')
    id_recipe= db.Column(db.Integer, db.ForeignKey('recipe.id'))
    recipe = db.relationship('Recipe', backref='recipe_in_recipe_menu')
  
  

    def __repr__(self):
        return '<Recipe_menu %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "id_menu": self.id_menu,
            "id_recipe": self.id_recipe,
            
            
        }