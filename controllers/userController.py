from flask import request, jsonify
from models.schemas.userSchema import user_schema
from services import userService
from marshmallow import ValidationError
from utils.util import role_required

@role_required('admin')
def login():
    user_request = request.json
    user = userService.login_user(user_request['username'], user_request['password'])
    if user:
        return jsonify(user), 200
    else:
        resp = {
            'status': 'Error',
            'message': 'User does not exist'
        }
    return jsonify(resp), 404