from sqlalchemy.orm import Session
from sqlalchemy.sql import select
from database import db
from models.user import User
from utils.util import encode_token

def login_user(username, password):
    user = (db.session.execute(db.select(User).where(User.username == username, User.password == password)).scalar_one_or_none())
    role_names = [role.role_name for role in user.roles]
    if user:
        auth_token = encode_token(user.id, role_names)
        resp = {
            'status': 'success',
            'message': 'Successfully logged in',
            'auth_token': auth_token
        }
        return resp
    else:
        return None