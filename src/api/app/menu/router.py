from flask import Flask, request, jsonify, url_for, Blueprint
from api.models.index import db, Recipe, User
from api.app.menu import controller
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity
from datetime import datetime

from logging import getLogger

logger = getLogger(__name__)

menus = Blueprint('menus', __name__)

@menus.route('/<assignation_date>', methods=['GET'])
@jwt_required()
def get_menu(assignation_date):
    assignation_date = datetime.strptime(assignation_date, "%Y-%m-%dT%H:%M:%S.%fZ")
    menu = controller.get_menu(assignation_date)
    if menu is None:
        return jsonify('menu not found'), 404
    else:
        return jsonify(menu), 200

