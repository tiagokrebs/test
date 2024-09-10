from flask import Blueprint, jsonify, request
from . import auth

bp = Blueprint('orders', __name__, url_prefix='/orders')

@bp.route('/', methods=['POST'])
@auth.login_required
def create_order():
    data = request.json

    # TODO: validate data
    if not data.get('user_id') or not data.get('product_id') or not data.get('quantity') or not data.get('price'):
        return jsonify({'message': 'Invalid data'}), 400
    #else:
        # TODO: insert into kafka 
    
    return jsonify({'message': 'Success'})


    
