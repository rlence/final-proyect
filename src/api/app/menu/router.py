from flask import Flask, request, jsonify, url_for, Blueprint
from api.models.index import db, Recipe, User
from api.app.menu import controller
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity
from datetime import datetime
from api.utils import APIException


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


@menus.route('/auto', methods=['POST'])
@jwt_required()
def generate_auto_menu():
    body = request.get_json()
    if body is None:
        logger.error("missing body")
        raise APIException(status_code=400, payload={
            'error': {
                'message': "missing body",
            }
        })
    if body.get('assignation_date') is None:
        logger.error("missing assignation date")
        raise APIException(status_code=400, payload={
            'error': {
                'message': "missing assignation date",
            }
        })

    body['assignation_date'] = datetime.strptime(body.get('assignation_date'), "%Y-%m-%dT%H:%M:%S.%fZ")
    body['id_user'] = get_jwt_identity()['id']

    
    new_auto_menu = controller.generate_auto_menu(body)

    return jsonify(new_auto_menu), 201


@menus.route('/recipe_menu/<id_recipe_menu>', methods=['PUT'])
@jwt_required()
def change_recipe_menu(id_recipe_menu):
    body = request.get_json()
    if body is None:
        logger.error("missing body")
        raise APIException(status_code=400, payload={
            'error': {
                'message': "missing body",
            }
        })
    if body.get('id_recipe') is None:
        logger.error("missing id recipe menu")
        raise APIException(status_code=400, payload={
            'error': {
                'message': "missing id recipe menu",
            }
        })

    controller.change_recipe_menu(id_recipe_menu, body['id_recipe'])

    return jsonify(), 202