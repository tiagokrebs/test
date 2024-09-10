import jwt
from flask import Blueprint, jsonify, request
import functools

bp = Blueprint('auth', __name__, url_prefix='/auth')

def create_token(user_id):
    return jwt.encode({'user_id': user_id}, 'secret', algorithm='HS256')

def verify_token(token):
    return jwt.decode(token, 'secret', algorithms=['HS256'])

@bp.route('/register', methods=['POST'])
def register():
    data = request.json
    user_id = data['user_id']
    token = create_token(user_id)

    # TODO: Insert into database

    return jsonify({'message': 'Success', 'token': token})

@bp.route('/login', methods=['POST'])
def login():
    data = request.json
    token = data['token']

    # TODO: Check if user exists in database

    return jsonify({'message': 'Success'})

@bp.before_app_request
def before_request():
    token = request.headers.get('Authorization')
    if token:
        try:
            request.user_id = verify_token(token)

            # TODO: Check if user exists in database

        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token expired'}), 401

def login_required(f):
    # maintain the metadata of the function
    # @functools.wraps(f)
    def view(*args, **kwargs):
        if not request.headers.get('Authorization'):
            return jsonify({'message': 'Unauthorized'}), 401
        return f(*args, **kwargs)
    return view