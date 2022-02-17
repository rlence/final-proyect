from flask import Flask, request, jsonify, url_for, Blueprint
from api.app.post.controller import create_post
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

posts = Blueprint('posts', __name__)

@posts.route("/create", methods=['POST'])
@jwt_required()
def post_create():
    user_id = get_jwt_identity()
    body = request.get_json()
    return create_post(body, user_id['id']) 
