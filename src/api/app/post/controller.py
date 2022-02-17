from api.models.index import db, Post
from api.shared.respose import succes_respose, error_response

def get_post_by_id():
    pass

def create_post(post, user_id):
    try:
        if post['message'] is None:
            return error_response('Bad Request', 400)
        new_post = Post(post=post['message'], user_id=user_id)
        db.session.add(new_post)
        db.session.commit()
        return succes_respose(new_post.serialize(), 201)
        
    except Exception as error:
        print('[ERROR POST CREATE]: ', error)
        db.session.rollback()
        return error_response('Internal Server Error', 500)
    