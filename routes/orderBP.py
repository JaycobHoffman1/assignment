from flask import Blueprint
from controllers.orderController import save, find_all_pagination, find_top_selling_products, find_num_of_products_produced

order_blueprint = Blueprint('order_bp', __name__)
order_blueprint.route('/', methods=['POST'])(save)
order_blueprint.route('/paginate', methods=['GET'])(find_all_pagination)
order_blueprint.route('/top-selling-products', methods=['GET'])(find_top_selling_products)
order_blueprint.route('/products-produced', methods=['GET'])(find_num_of_products_produced)