from flask import Flask, request, jsonify, url_for, Blueprint
from api.app.recipe.controller import create_recipe, get_recipe, get_recipe_list, update_recipe
from api.app.recipe import controller
from cloudinary.uploader import upload

recipes = Blueprint('recipes', __name__)

@recipes.route('/create', methods=["POST"])
def create_recipe():
    body = request.get_json()

    new_recipe = controller.create_recipe(body)
    if new_recipe is None:
        return jsonify('Internal server error'), 500
    elif new_recipe == False:
        return jsonify('Bad Request'), 400
    else:
        return jsonify(new_recipe), 201

@recipes.route('/img', methods=["POST"])
def upload_file():
    try:
        img = request.files['img']
        url_img = upload(img)
       
            
        return jsonify(url_img['url'],200)
    except Exception as error:
        print(error)
        return jsonify('error al guardar la imagen', 500)

@recipes.route('/get/<id>', methods = ['GET'])
def get_recipe(id):
    recipe = controller.get_recipe(id)

    return jsonify(recipe.serialize())

@recipes.route('/update/<id>', methods = ['PUT'])
def update_recipe(id):
    body = request.get_json()

    return jsonify(controller.update_recipe(id, body))

@recipes.route('/', methods=['GET'])
def get_recipe_list():
    page = int(request.args.get('page', 1))
    search = request.args.get('search')
    recipe_list =  controller.get_recipe_list(page=page, search=search)

    return jsonify(recipe_list), 200