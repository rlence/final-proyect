from api.utils import APIException
from sqlalchemy.exc import IntegrityError
from sqlalchemy import func
from datetime import datetime, timedelta

from api.models.index import db, Menu
from logging import getLogger

logger = getLogger(__name__)


def get_menu(assignation_date):
    try:
        first_day_of_week = assignation_date - timedelta(days=assignation_date.weekday())
        last_day_of_week = first_day_of_week + timedelta(days=6)
        menu = Menu.query.filter(
            func.date(Menu.assignation_date) >= first_day_of_week,
            func.date(Menu.assignation_date) <= last_day_of_week).first()
        if not menu:
            return None

        recipe_list = []
        recipe_menu_list = menu.recipe_menu
        for recipe_menu in recipe_menu_list:
            recipe_list.append({
                "id": recipe_menu.recipe.id,
                "title": recipe_menu.recipe.title,
                "selected_tag": recipe_menu.selected_tag,
                "selected_date": recipe_menu.selected_date,
            })

        return {
            **menu.serialize(),
            'recipe_list': recipe_list
        }
    except Exception as error:
        logger.error("Error getting menu")
        logger.exception(error)
        raise APIException(status_code=400, payload={
            'error': {
                'message': "Error getting menu",
            }
        })