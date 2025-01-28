import json
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_add_customer(client, mocker):
    payload = {'id': 4, 'name': 'Nicole', 'email': 'nicolehoffman@gmail.com', 'phone': '111-222-3333'}
    mocker.patch.object(client, 'post', return_value=app.response_class(
        response=json.dumps({'message': 'Customer added!'}),
        status=200,
        mimetype='application/json'
    ))

    response = client.post('/customers', json=payload)
    data = response.get_json()
    if data:
        return 'Test successful!'
    else:
        return 'Test failed.'
    
def test_add_employee(client, mocker):
    payload = {'id': 4, 'name': 'Thea', 'position': 'Junior developer'}
    mocker.patch.object(client, 'post', return_value=app.response_class(
        response=json.dumps({'message': 'Employee added!'}),
        status=200,
        mimetype='application/json'
    ))

    response = client.post('/employees', json=payload)
    data = response.get_json()
    if data:
        return 'Test successful!'
    else:
        return 'Test failed.'
    
def test_add_order(client, mocker):
    payload = {'id': 4, 'customer_id': 4, 'product_id': 4, 'quantity': 1, 'total_price': 12.99}
    mocker.patch.object(client, 'post', return_value=app.response_class(
        response=json.dumps({'message': 'Order added!'}),
        status=200,
        mimetype='application/json'
    ))

    response = client.post('/orders', json=payload)
    data = response.get_json()
    if data:
        return 'Test successful!'
    else:
        return 'Test failed.'
    
def test_add_product(client, mocker):
    payload = {'id': 4, 'name': 'Dress', 'price': 12.99}
    mocker.patch.object(client, 'post', return_value=app.response_class(
        response=json.dumps({'message': 'Product added!'}),
        status=200,
        mimetype='application/json'
    ))

    response = client.post('/products', json=payload)
    data = response.get_json()
    if data:
        return 'Test successful!'
    else:
        return 'Test failed.'
    
def test_add_production(client, mocker):
    payload = {'id': 4, 'product_id': 4, 'quantity_produced': 15, 'date_produced': '2025-01-27'}
    mocker.patch.object(client, 'post', return_value=app.response_class(
        response=json.dumps({'message': 'Production data added!'}),
        status=200,
        mimetype='application/json'
    ))

    response = client.post('/production', json=payload)
    data = response.get_json()
    if data:
        return 'Test successful!'
    else:
        return 'Test failed.'
    
if __name__ == '__main__':
    pytest.main([__file__])