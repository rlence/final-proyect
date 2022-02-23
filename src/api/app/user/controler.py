from api.shared.encrypte_pass import encryp_pass, compare_pass
from api.models.index import db, User
from flask_jwt_extended import create_access_token

def get_user_by_id(user_id):
    return User.query.get(user_id)

def register_user(body):
    try:
        if not body:
            return False

        if body['password'] is None:
            return False

        if body['email'] is None:
            return False
        
        if body['name'] is None:
            return False

        hash_pass = encryp_pass(body['password'])
        new_user = User(email=body['email'], password=hash_pass, name=body['name'], last_name=body['last_name'])
        db.session.add(new_user)
        db.session.commit()
        return new_user.serialize()

    except Exception as err:
        db.session.rollback()
        print('[ERROR REGISTER USER]: ', err)
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

        new_token = create_access_token(identity={'id': current_user.id})
        return { 'token': new_token }
        
    except Exception as err:
        print('[ERROR LOGIN]: ', err)
        return None