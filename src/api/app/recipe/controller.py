from sqlalchemy.exc import IntegrityError,InvalidRequestError

from api.utils import APIException

from api.models.index import db, Recipe, User, Ingredient, Recipe_ingredient,MyRecipe


from logging import getLogger

logger = getLogger(__name__)

def create_recipe(body, url_img):

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
        "private": body.get('private'),
        "id_user": body.get('id_user'), 

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


    try:
        new_recipe = Recipe(**recipe_info)
        db.session.add(new_recipe)
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
        my_new_recipe =MyRecipe(**my_recipe_info)
        db.session.add(my_new_recipe)
        db.session.commit()

    except Exception as error:
        print("Error saving recipe:", error)
        db.session.rollback()
        return None


def get_recipe(recipe_id):
    try:   
        return Recipe.query.get(recipe_id)

    except Exception as error:
        logger.error("Error getting recipe")
        logger.exception(error)
        raise APIException(status_code=400, payload={
            'error': {
                'message': "Error getting recipe",
            }
        })



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

#get list recipies from my_recipe    
def get_myrecipe_list(user_id,page=1, per_page=20):
    
        recipe_page = MyRecipe.query.filter_by(id_user=user_id).paginate(page,per_page)
        print(recipe_page)
        
        recipe_list = [] 
        for recipe in recipe_page.items:
            recipe_list.append(recipe.serialize()) 

        return dict(
            items=recipe_list, 
            total=recipe_page.total, 
            current_page=recipe_page.page
        )


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


    
  
