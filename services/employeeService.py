from sqlalchemy.orm import Session
from database import db
from models.employee import Employee

def save(employee_data):
    with Session(db.engine) as session:
        with session.begin():
            new_employee = Employee(id=employee_data['id'], name=employee_data['name'], email=employee_data['email'], position=employee_data['position'])
            session.add(new_employee)
            session.commit()

        session.refresh(new_employee)
        return new_employee