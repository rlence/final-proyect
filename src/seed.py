import os
from api.db.seed_data import data
from sqlalchemy import insert
import api.models.index as models
from flask import Flask
from flask_migrate import Migrate


def load_seed():
    for table, rows in data.items():
        ModelClass = getattr(models, table)
        for row in rows:
            inserted = insert(ModelClass).values(**row)
            try:
                models.db.session.execute(inserted)
                models.db.session.commit()
            except Exception as e:
                print(f'ERROR: inserting row {row} in "{table}". IGNORING')
                print(e)

if __name__ == "__main__":
    app = Flask(__name__)
    uri = os.getenv("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    app.config['SQLALCHEMY_DATABASE_URI'] = uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    models.db.init_app(app)
    MIGRATE = Migrate(app, models.db)
    with app.app_context():
        load_seed()