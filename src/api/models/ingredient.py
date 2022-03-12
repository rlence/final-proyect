from api.models.db import db

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False)

    # in_recipes = db.relationship('Recipe_ingredient', backref='ingredient')

    def __repr__(self):
        return '<Ingredient %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
        }