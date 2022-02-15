from flask import Flask, request, jsonify, url_for, Blueprint
from api.app.user.controler import register_user, login_user, get_user_by_id
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

users = Blueprint('users', __name__)

@users.route('/register', methods=['POST'])
def create_user():
    body = request.get_json()
    new_user = register_user(body)
    if new_user is None:
        return jsonify('Internal server error'), 500
    elif new_user == False:
        return jsonify('Bad Request'), 400
    else:
        return jsonify(new_user), 201

@users.route('/login', methods=['POST'])
def user_login():
    body = request.get_json()
    token = login_user(body)

    if token == 'user not exist':
        return jsonify(token), 404

    elif token == 'pass not iqual':
        return jsonify('user or password incorrect'), 401

    elif token is None :
        return jsonify('Internal server error'), 500
    else:
        return jsonify(token), 200

@users.route("/", methods=['GET'])
@jwt_required()
def get_user():
    user_id = get_jwt_identity()
    user = get_user_by_id(user_id['id'])
    if user is None:
        return jsonify('user not found'), 404

    return jsonify(user.serialize()), 200