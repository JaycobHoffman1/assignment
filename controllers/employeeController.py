from flask import request, jsonify
from models.schemas.employeeSchema import employee_schema
from services import employeeService
from marshmallow import ValidationError
from utils.util import role_required

@role_required('admin')
def save():
    try:
        employee_data = employee_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    employee_save = employeeService.save(employee_data)
    return employee_schema.jsonify(employee_save), 201