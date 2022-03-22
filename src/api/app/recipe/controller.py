import json
import math
from flask_jwt_extended import get_jwt_identity

from sqlalchemy.exc import IntegrityError,InvalidRequestError

from api.utils import APIException

from api.models.index import db, Recipe, User, RecipeIngredient, Ingredient, MyRecipe


from logging import getLogger

logger = getLogger(__name__)

def create_recipe(body, url_img=None):

    if not body:
        raise APIException(status_code=400, payload={
            'error': {
                'message': 'missing body',
            }
        })

    recipe_info = {
        "photo":url_img,
        "title":body.get('title'),
        "description": body.get('description'),
        "private": bool(body.get('private')),
        "id_user": body.get('id_user'), 
        "tag": body.get('tag')           
    }

    if recipe_info['title'] is None:
        logger.error("missing title")
        raise APIException(status_code=400, payload={
            'error': {
                'message': 'missing title',
            }
        })

    if recipe_info['description'] is None:
        logger.error("missing description")
        raise APIException(status_code=400, payload={
            'error': {
                'message': 'missing description',
            }
        })

    try:
        new_recipe = Recipe(**recipe_info)
        db.session.add(new_recipe)
        db.session.flush()
        ingredient_list = []
        ingredient_list_raw = json.loads(body.get('ingredient_list')) if body.get('ingredient_list') else []
        for ingredient_raw in ingredient_list_raw:
            db.session.add(RecipeIngredient(id_ingredient=int(ingredient_raw['id']), id_recipe=new_recipe.id))

        db.session.commit()
        return new_recipe.serialize()
    except Exception as error:
        print("Error creating recipe:", error)
        db.session.rollback()
        return None

def save_in_my_recipe(body,recipe_id):
    my_recipe_info={
        "id_recipe":recipe_id,
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
    if my_recipe_info['id_user'] is None:
        logger.error("missing id_user")
        raise APIException(status_code=400, payload={
            'error': {
                'message': 'missing id_user',
            }
        })    
   
    try:
        my_new_recipe = MyRecipe(**my_recipe_info)
        db.session.add(my_new_recipe)
        db.session.commit()

    except Exception as error:
        print("Error saving recipe:", error)
        db.session.rollback()
        return None


def get_recipe(recipe_id):
    try:
        recipe = Recipe.query.get(recipe_id)
        if not recipe:
            return None 
        
        ingredient_list = []
        recipe_ingredient_list = recipe.recipe_ingredients
        for recipe_ingredient in recipe_ingredient_list:
            ingredient_list.append(recipe_ingredient.ingredient.serialize())

        return {
            **recipe.serialize(),
            'ingredient_list': ingredient_list
        }
    except Exception as error:
        logger.error("Error getting recipe")
        logger.exception(error)
        raise APIException(status_code=400, payload={
            'error': {
                'message': "Error getting recipe",
            }
        })



def get_recipe_list(page=1, per_page=20, search=None):

    if not search :
        recipe_page = Recipe.query.paginate(page,per_page)
        
    else:
        recipe_page = Recipe.query.filter(Recipe.title.ilike(f'%{search}%')).paginate(page,per_page)
       

    recipe_list = [] 
    for recipe in recipe_page.items:
        recipe_list.append(recipe.serialize()) 

    return dict(
        items=recipe_list, 
        total_items=recipe_page.total, 
        current_page=recipe_page.page,
        total_pages =math.ceil(recipe_page.total/per_page)
    )

#get list recipies from my_recipe    
def get_myrecipe_list(user_id):
    
        my_recipe_list = MyRecipe.query.filter(MyRecipe.id_user==user_id)
       
        serialized_my_recipe_list = [] 
        for my_recipe in my_recipe_list:
            serialized_my_recipe_list.append(my_recipe.serialize()) 

        return serialized_my_recipe_list



def update_recipe(recipe_id, recipe_params):
    """
    Updates an existing recipe with new data

    :param recipe_id: id of the recipe to update
    :param recipe_params: a dict with the fields to update in the existing recipe
    """
    try:
       
        num_rows_updated = Recipe.query.filter_by(id=recipe_id).update(recipe_params)
        db.session.commit()
        return  Recipe.query.get(recipe_id)

    except InvalidRequestError as error:
        db.session.rollback()
        logger.error(error)
        invalid_key = str(error).split(' ')[-1]
        raise APIException(status_code=400, payload={
            'error': {
                'message': f"Error, invalid key {invalid_key}",
            }
        })

    except Exception as error:
        logger.error("Error updating recipe")
        logger.exception(error)
        raise APIException(status_code=400, payload={
            'error': {
                'message': "Error updating recipe",
            }
        })


    
  
