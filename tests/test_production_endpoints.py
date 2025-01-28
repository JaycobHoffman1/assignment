import unittest
from unittest import mock
from app import app

class TestProductionEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_add_production1(self):
        payload = {'id': 1, 'product_id': 1, 'quantity_produced': 10, 'date_produced': '2025-01-26'}
        response = self.app.post('/productions', json=payload)
        data = response.get_json()
        if data:
            return 'Test successful!'
        return 'Test failed.'
    
    def test_add_production2(self):
        payload = {'id': 2, 'product_id': 2, 'quantity_produced': 20, 'date_produced': '2025-01-25'}
        response = self.app.post('/productions', json=payload)
        data = response.get_json()
        if data:
            return 'Test successful!'
        return 'Test failed.'
    
    def test_add_production2(self):
        payload = {'id': 3, 'product_id': 3, 'quantity_produced': 30, 'date_produced': '2025-01-24'}
        response = self.app.post('/production', json=payload)
        data = response.get_json()
        if data:
            return 'Test successful!'
        return 'Test failed.'
    
if __name__ == '__main__':
    unittest.main()