from flask import request, jsonify
from models.schemas.orderSchema import order_schema, orders_schema
from services import orderService
from marshmallow import ValidationError
from utils.util import role_required

@role_required('user')
def save():
    try:
        order_data = order_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    order_save = orderService.save(order_data)
    return order_schema.jsonify(order_save), 201

def find_all_pagination():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    return orders_schema.jsonify(orderService.find_all_pagination(page=page, per_page=per_page)), 200

def find_top_selling_products():
    top_selling_products = orderService.find_top_selling_products()
    return order_schema.jsonify(top_selling_products), 200

def find_num_of_products_produced():
    num_of_products_produced = orderService.find_num_of_products_produced()
    return order_schema.jsonify(num_of_products_produced), 200