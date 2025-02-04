from flask import Flask
from database import db
from schema import ma
from limiter import limiter
from sqlalchemy.orm import Session

from models.customer import Customer
from models.employee import Employee
from models.order import Order
from models.product import Product
from models.production import Production
from models.user import User
from models.role import Role
from flask_swagger_ui import get_swaggerui_blueprint

from routes.customerBP import customer_blueprint
from routes.employeeBP import employee_blueprint
from routes.orderBP import order_blueprint
from routes.productBP import product_blueprint
from routes.productionBP import production_blueprint
from routes.userBP import user_blueprint

SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.yaml'

swaggerui_bluerint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'Factory API'
    }
)

def create_app():
    app = Flask(__name__)

    app.config.from_object('config.DevelopmentConfig')
    db.init_app(app)
    ma.init_app(app)
    limiter.init_app(app)

    return app

def blue_print_config(app):
    app.register_blueprint(customer_blueprint, url_prefix='/customers')
    app.register_blueprint(employee_blueprint, url_prefix='/employees')
    app.register_blueprint(order_blueprint, url_prefix='/orders')
    app.register_blueprint(product_blueprint, url_prefix='/products')
    app.register_blueprint(production_blueprint, url_prefix='/production')
    app.register_blueprint(user_blueprint, url_prefix='/users')

def configure_rate_limit():
    limiter.limit('5 per day')(customer_blueprint)
    limiter.limit('5 per day')(employee_blueprint)
    limiter.limit('5 per day')(order_blueprint)
    limiter.limit('5 per day')(product_blueprint)
    limiter.limit('5 per day')(production_blueprint)
    limiter.limit('5 per day')(user_blueprint)

def init_roles_data():
    with Session(db.engine) as session:
        with session.begin():
            roles = [
                Role(role_name = 'admin'),
                Role(role_name = 'user')
            ]
            session.add_all(roles)

if __name__ == '__main__':
    app = create_app()

    blue_print_config(app)
    configure_rate_limit()

    with app.app_context():
        db.drop_all()
        db.create_all()
        init_roles_data()

    app.run(debug=True)