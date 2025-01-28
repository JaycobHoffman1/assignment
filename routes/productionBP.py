from flask import Blueprint
from controllers.productionController import save, find_num_of_products_produced, evaluate_production_efficiency

production_blueprint = Blueprint('production_bp', __name__)
production_blueprint.route('/', methods=['POST'])(save)
production_blueprint.route('/products-produced', methods=['GET'])(find_num_of_products_produced)
production_blueprint.route('/production-efficiency', methods=['GET'])(evaluate_production_efficiency)