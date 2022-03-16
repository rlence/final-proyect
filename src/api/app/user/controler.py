from datetime import timedelta
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token

from api.utils import APIException
from api.shared.encrypte_pass import encryp_pass, compare_pass
from api.models.index import db, User

from logging import getLogger

logger = getLogger(__name__)

def get_user_by_id(user_id):
    return User.query.get(user_id)

def register_user(body):
    try:
        if not body:
            return False
        
        user_info = {
            "password": body.get('password'),
            "email": body.get('email'),
            "name": body.get('name'),
            "last_name": body.get('lastName'),
        }
        if user_info['password'] is None:
            return False

        if user_info['email'] is None:
            return False
        
        if user_info['name'] is None:
            return False

        hash_pass = encryp_pass(user_info['password'])
        user_info['password'] = hash_pass

        new_user = User(**user_info)
        db.session.add(new_user)
        db.session.commit()
        return login_user({'email': body['email'], 'password':body['password']})
    except IntegrityError as err:
        logger.exception('[ERROR REGISTER USER]: USER DUPLICATED ')
        raise APIException(status_code=401, payload={
            'error': {
                'message': 'Email no valido',
            }
        })
    except Exception as err:
        db.session.rollback()
        logger.exception('[ERROR REGISTER USER]: Unexepcted')
        return None


def login_user(body):
    try:
        if body['password'] is None:
            return False

        if body['email'] is None:
            return False

        current_user = db.session.query(User).filter(User.email == body['email']).first()
        if current_user is None:
            return 'user not exist'

        validate_pass = compare_pass(body['password'], current_user.password)
        if validate_pass == False:
            return 'pass not iqual'

        new_token = create_access_token(identity={'id': current_user.id}, expires_delta=timedelta(weeks=4))
        return { 'token': new_token }
        
    except Exception as err:
        print('[ERROR LOGIN]: ', err)
        return None