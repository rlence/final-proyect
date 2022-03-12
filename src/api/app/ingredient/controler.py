from sqlalchemy.exc import IntegrityError

from api.utils import APIException
from api.models.index import db, Ingredient, Recipe_ingredient

from logging import getLogger

logger = getLogger(__name__)


def list_ingredient(page=1, per_page=20, search=""):
    ingredient_page = Ingredient.query.filter(Ingredient.name.ilike(f'%{search}%')).paginate(page,per_page)
    
    ingredient_list = [] 
    for ingredient in ingredient_page.items:
        ingredient_list.append(ingredient.serialize()) 

    return dict(
        items=ingredient_list, 
        total=ingredient_page.total, 
        current_page=ingredient_page.page
    )


def create_ingredient(body):
    try:
        if not body:
            return False
        
        ingredient_info = {
            "name": body.get('name'),
        }
        
        if ingredient_info['name'] is None:
            return False

        new_ingredient = Ingredient(**ingredient_info)
        db.session.add(new_ingredient)
        db.session.commit()
        return new_ingredient.serialize()
    except IntegrityError as err:
        logger.exception('[ERROR CREATE INGREDIENT]: INGREDIENT DUPLICATED ')
        raise APIException(status_code=401, payload={
            'error': {
                'message': 'Ya existe este ingrediente',
            }
        })
    except Exception as err:
        db.session.rollback()
        logger.exception('[ERROR CREATE INGREDIENT]: Unexepcted')
        return None

# when create recipe, back send to front the recipe id, then front send id_ingredient, quantity and id_recipe
def create_ingredient_recipe(body): 
    #body array of dicts: id_ingredient, id_recipe and quantity
    try:
        if not body:
            return False
        
        ingredient_info = {
            "quantity":body.get('quantity'),
            "id_ingredient":body.get('id_ingredient'),
            "id_recipe":body.get('id_recipe'),
        }
        
        if ingredient_info['quantity'] is None:
            return False

        new_recipe_ingredient = Recipe_ingredient(**ingredient_info)
        db.session.add(new_recipe_ingredient)
        db.session.commit()
        return new_recipe_ingredient.serialize()

    except Exception as err:
        db.session.rollback()
        logger.exception('[ERROR CREATE INGREDIENT]: Unexepcted')
        return None
