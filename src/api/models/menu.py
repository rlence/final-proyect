from api.models.db import db

class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    create_at = db.Column(db.Date)
    assignation_date = db.Column(db.Date)
    id_user= db.Column(db.Integer, db.ForeignKey('user.id'))
    recipe_menu = db.relationship(
                    'RecipeMenu',
                    cascade="all,delete",
                    order_by='RecipeMenu.selected_date',
                )
    user = db.relationship('User', backref='user_menu')


    def __repr__(self):
        return '<Menu %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "create_at": self.create_at.isoformat(),
            "id_user": self.id_user,
        }