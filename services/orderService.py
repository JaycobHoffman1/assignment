from sqlalchemy.orm import Session
from sqlalchemy.sql import select, func
from database import db
from models.order import Order
from models.customer import Customer

def save(order_data):
    with Session(db.engine) as session:
        with session.begin():
            new_order = Order(id=order_data['id'], customer_id=order_data['customer_id'], product_id=order_data['product_id'], quantity=order_data['quantity'], total_price=order_data['total_price'])
            session.add(new_order)
            session.commit()

        session.refresh(new_order)
        return new_order

def find_all_pagination(page=1, per_page=10):
    orders = db.paginate(select(Order), page=page, per_page=per_page)
    return orders

def find_top_selling_products():
    query = select(Order.quantity).group_by(Order.customer_id)
    top_selling_products = db.session.execute(query).scalars().all()

    return top_selling_products

def find_num_of_products_produced():
    query = select(func.sum(Order.total_price)).group_by(Customer.name).having(Order.total_price > 3.99)
    num_of_products_produced = db.session.execute(query).scalars().all()

    return num_of_products_produced