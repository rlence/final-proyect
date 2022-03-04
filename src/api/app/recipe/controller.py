from sqlalchemy.exc import IntegrityError

from api.utils import APIException
from api.models.index import db, Recipe, User

from logging import getLogger

logger = getLogger(__name__)

def create_recipe(body):

    if not body:
        raise APIException(status_code=400, payload={
            'error': {
                'message': 'missing body',
            }
        })

    recipe_info = {
        "photo": body.get('photo'),
        "title":body.get('title'),
        "description": body.get('description'),
        "private": body.get('private'),
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
    

    new_recipe = Recipe(**recipe_info)
    db.session.add(new_recipe)
    db.session.commit()
    return new_recipe.serialize()


def get_recipe(recipe_id):
    return Recipe.query.get(recipe_id)

def get_recipe_list(page=1, per_page=20, search=""):
    recipe_page = Recipe.query.filter(Recipe.title.ilike(f'%{search}%')).paginate(page,per_page)
    print(recipe_page)
    
    recipe_list = [] 
    for recipe in recipe_page.items:
        recipe_list.append(recipe.serialize()) 

    return dict(
        items=recipe_list, 
        total=recipe_page.total, 
        current_page=recipe_page.page
    )
# def get_list_recipes():
#     recipes = Recipe.query.get_all()

#     recipes_list = []
#     for recipe in recipes:
#         recipes_list.append(recipes.serialize())

#     return jsonify(recipes_list)

def update_recipe(recipe_id, recipe_params):
    """
    Updates an existing recipe with new data

    :param recipe_id: id of the recipe to update
    :param recipe_params: a dict with the fields to update in the existing recipe
    """
    num_rows_updated = Recipe.query.filter_by(id=recipe_id).update(recipe_params)
    db.session.commit()
    recipe = Recipe.query.get(recipe_id)
    return recipe.serialize()


    
  
