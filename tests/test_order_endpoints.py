import unittest
from app import app

class TestOrderEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_add_order1(self):
        payload = {'id': 1, 'customer_id': 1, 'product_id': 1, 'quantity': 3, 'total_price': 9.99}
        response = self.app.post('/orders', json=payload)
        data = response.get_json()
        if data:
            return 'Test successful!'
        return 'Test failed.'
    
    def test_add_order2(self):
        payload = {'id': 2, 'customer_id': 2, 'product_id': 2, 'quantity': 1, 'total_price': 4.99}
        response = self.app.post('/orders', json=payload)
        data = response.get_json()
        if data:
            return 'Test successful!'
        return 'Test failed.'
    
    def test_add_order2(self):
        payload = {'id': 3, 'customer_id': 3, 'product_id': 3, 'quantity': 2, 'total_price': 6.99}
        response = self.app.post('/orders', json=payload)
        data = response.get_json()
        if data:
            return 'Test successful!'
        return 'Test failed.'
    
if __name__ == '__main__':
    unittest.main()