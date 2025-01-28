from sqlalchemy.orm import Session
from database import db
from sqlalchemy.sql import select, func
from database import db
from models.production import Production
from models.product import Product
from models.employee import Employee

def save(production_data):
    with Session(db.engine) as session:
        with session.begin():
            new_production = Production(id=production_data['id'], product_id=production_data['product_id'], quantity_produced=production_data['quantity_produced'], date_produced=production_data['date_produced'])
            session.add(new_production)
            session.commit()

        session.refresh(new_production)
        return new_production
    
def find_num_of_products_produced():
    query = select(func.sum(Production.quantity_produced)).group_by(Employee.name)
    num_of_products_produced = db.session.execute(query).scalars().all()

    return num_of_products_produced

def evaluate_production_efficiency(date):
    query = select(Production).join(Product).where(Product.id == Production.product_id).filter_by(date=Production.date_produced).group_by(Product.name)
    production_efficiency = db.session.execute(query).scalars().all()

    return production_efficiency