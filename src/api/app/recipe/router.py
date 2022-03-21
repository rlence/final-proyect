from flask import Flask, request, jsonify, url_for, Blueprint


from api.app.recipe import controller
from cloudinary.uploader import upload
import cloudinary
from api.utils import APIException
from flask_jwt_extended import jwt_required

from flask_jwt_extended import get_jwt_identity
from api.models.index import db, Recipe, User, Ingredient, RecipeIngredient, MyRecipe



from logging import getLogger

logger = getLogger(__name__)

recipes = Blueprint('recipes', __name__)


# form data with img, tag and general recipe data

@recipes.route('/create', methods=["POST"])
@jwt_required()
def create_recipe():
    img = request.files.get('img')
    if img:
        try:
            img = upload(img)["url"] 
        except Exception as error:
            logger.error("Error uploading img to cloudinary")
            logger.exception(error)
            raise APIException(status_code=400, payload={
                'error': {
                    'message': 'Error uploading img to cloudinary',
                }
            })


    body = request.form.to_dict()
    body['id_user'] = get_jwt_identity()['id']
    new_recipe = controller.create_recipe(body, img)
    
    if new_recipe is None:
        return jsonify('Internal server error'), 500
    if new_recipe == False:
        return jsonify('Bad Request'), 400
   
    #save the recipe created in my_recipe:
    controller.save_in_my_recipe(body, new_recipe["id"])

    return jsonify(new_recipe), 201


#save public recipe in MyRecipe: body with recipe_id, id_user and tag
@recipes.route('/myrecipes/save', methods=["POST"])
@jwt_required()
def save_in_my_recipe():       
    body = request.get_json()
    recipe_id = body.get('id_recipe')
   
    if recipe_id is None:
        logger.error("missing recipe_id")
        raise APIException(status_code=400, payload={
            'error': {
                'message': "missing recipe_id",
            }
        })
    controller.save_in_my_recipe(body,recipe_id)

    return jsonify("Recipe saved correctly"), 201

# get for my_recipes, private recipes with token
@recipes.route('/myrecipes/get/<id>', methods = ['GET'])
@jwt_required()
def get_my_recipe(id):
   
    recipe = controller.get_recipe(id)
    if recipe is None:
        return jsonify('user not found'), 404

    if recipe.get("private"):
        user_token=get_jwt_identity()
        user=User.query.get(user_token)
        if user.id != recipe['id_user']:
             raise APIException(status_code= 403, payload={
                'error':{
                    'message': "This recipe is private, and belongs to another user"
                }
            })
            
    return jsonify(recipe)

       
# get for public recipes without token   
@recipes.route('/get/<id>', methods = ['GET'])
def get_recipe(id):           
    recipe = controller.get_recipe(id)
    return jsonify(recipe.serialize())

    
#update a recipe I have created
@recipes.route('/update/<id>', methods = ['PUT'])
@jwt_required()
def update_recipe(id):
    body = request.get_json()
    recipe = (controller.update_recipe(id, body))

    return jsonify(recipe.serialize())

#get public recipes_list
@recipes.route('/', methods=['GET'])
def get_recipe_list():
    page = int(request.args.get('page', 1))
    search = request.args.get('search')
    recipe_list = controller.get_recipe_list(page=page, search=search)

    return jsonify(recipe_list), 200

#get private recipes list from my_recipies
@recipes.route('/myrecipes', methods=['GET'])
@jwt_required()
def get_myrecipe_list():
    user_token=get_jwt_identity()
    user=User.query.get(user_token)
    recipe_list =  controller.get_myrecipe_list(user.id)
    if user is None:
        return jsonify('user not found'), 404
    else:
        return jsonify(recipe_list), 200
    

#to update "tag":lunch, dinner, both" in public recipes saveded in my_recipe:
@recipes.route('/myrecipes/update/<id>', methods = ['PUT'])
@jwt_required()
def update_myrecipe(id):
    #recieved "tag" in body
    body = request.get_json()

    my_recipe_info={
        "id_recipe": id,
        "id_user": body.get('id_user'), 
        "tag" :body.get('tag')

    }

    if my_recipe_info['tag'] is None:
        logger.error("missing tag")
        raise APIException(status_code=400, payload={
            'error': {
                'message': 'missing tag',
            }
        })    

    my_new_recipe = MyRecipe(**my_recipe_info)
    db.session.add(my_new_recipe)
    db.session.commit()
    return jsonify("Tag changes save correctly in MyRecipes")

#delete public recipies in my_recipe
@recipes.route('/myrecipes/<id>', methods = ['DELETE'])
@jwt_required()
def delete_in_myrecipes(id):
    try:
        recipe=  MyRecipe.query.get(id)
        db.session.delete(recipe)
        db.session.commit()
        return jsonify('Recipe delete correctly')

    except Exception as error:
        print("Error deleting recipe:", error)
        db.session.rollback()
        return None

