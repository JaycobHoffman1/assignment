from flask import request, jsonify
from models.schemas.productionSchema import production_schema
from services import productionService
from marshmallow import ValidationError
from utils.util import role_required

@role_required('admin')
def save():
    try:
        production_data = production_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    production_save = productionService.save(production_data)
    return production_schema.jsonify(production_save), 201

def find_num_of_products_produced():
    num_of_products_produced = productionService.find_num_of_products_produced()
    return production_schema.jsonify(num_of_products_produced), 200

def evaluate_production_efficiency(date):
    production_effciency = productionService.evaluate_production_efficiency(date)
    return production_schema.jsonify(production_effciency), 200