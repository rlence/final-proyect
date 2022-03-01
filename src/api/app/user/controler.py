from api.shared.encrypte_pass import encryp_pass, compare_pass
from api.models.index import db, User
from flask_jwt_extended import create_access_token

def get_user_by_id(user_id):
    return User.query.get(user_id)

def register_user(body):
    try:
        if body['password'] is None:
            return False

        if body['email'] is None:
            return False

        hash_pass = encryp_pass(body['password'])
        new_user = User(email=body['email'], password=hash_pass)
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

        user = db.session.query(User).filter(User.email == body['email']).first()
        if user is None:
            return 'user not exist'

        validate_pass = compare_pass(body['password'], user.password)
        if validate_pass == False:
            return 'pass not iqual'

        new_token = create_access_token(identity={'id': user.id})
        return { 'token': new_token }
        
    except Exception as err:
        print('[ERROR LOGIN]: ', err)
        return None

def update_user_info(body, user_id):
    try:
        print("body", body)
        user = User.query.get(user_id)
        print(user)
        ## forma 1
       # user.email = body['email']
        print("update user")
        ## forma 2 
        user_json = user.json_to_update()
  
        for key, value in body.items():
            user_json[key] = value
    
        db.session.query(User).filter(User.id == user_id).update(user_json)
        db.session.commit()
        return user.serialize()
    except Exception as err:
        print(err)
        return None