"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for, send_from_directory
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from api.utils import APIException, generate_sitemap
from api.models.db import db
from api.app.user.router import users
from api.app.ingredient.router import ingredients

from api.app.recipe.router import recipes
from api.admin import setup_admin
from flask_jwt_extended import JWTManager

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

import cloudinary
import cloudinary.uploader
import cloudinary.api

#from models import Person

ENV = os.getenv("FLASK_ENV")
static_file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../public/')
app = Flask(__name__)
app.url_map.strict_slashes = False


# database condiguration
db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_KEY")
app.config["CLOUD_NAME"] = os.environ.get("CLOUD_NAME")
app.config["CLOUD_API_KEY"] = os.environ.get("CLOUD_API_KEY")
app.config["CLOUD_API_SECRET"] = os.environ.get("CLOUD_API_SECRET")

MIGRATE = Migrate(app, db, compare_type = True)
db.init_app(app)
jwt = JWTManager(app)

# Allow CORS requests to this API
CORS(app)

# add the admin
setup_admin(app)


app.register_blueprint(users, url_prefix="/api/user")
app.register_blueprint(ingredients, url_prefix="/api/ingredient")
app.register_blueprint(recipes, url_prefix="/api/recipe")

cloudinary.config( 
  cloud_name = app.config["CLOUD_NAME"], 
  api_key = app.config["CLOUD_API_KEY"], 
  api_secret = app.config["CLOUD_API_SECRET"],
  secure = True
)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    if ENV == "development":
        return generate_sitemap(app)
    return send_from_directory(static_file_dir, 'index.html')

# any other endpoint will try to serve it like a static file
@app.route('/<path:path>', methods=['GET'])
def serve_any_other_file(path):
    if not os.path.isfile(os.path.join(static_file_dir, path)):
        path = 'index.html'
    response = send_from_directory(static_file_dir, path)
    response.cache_control.max_age = 0 # avoid cache memory
    return response

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3001))
    app.run(host='0.0.0.0', port=PORT, debug=True)
