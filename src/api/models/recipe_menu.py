from api.models.db import db

class RecipeMenu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_menu= db.Column(db.Integer, db.ForeignKey('menu.id'))
    # menu = db.relationship('Menu', backref='menu_in_recipe_menu') 
    id_recipe= db.Column(db.Integer, db.ForeignKey('recipe.id'))
    selected_tag = db.Column(db.Integer, nullable=False)
    selected_date = db.Column(db.Date, nullable=False)
    recipe = db.relationship('Recipe')

  
    def __repr__(self):
        return '<RecipeMenu %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "id_menu": self.id_menu,
            "id_recipe": self.id_recipe,
        }