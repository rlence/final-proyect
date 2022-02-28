from sqlalchemy.exc import IntegrityError

from api.utils import APIException
from api.models.index import db, Ingredient

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


