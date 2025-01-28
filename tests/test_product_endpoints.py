import unittest
from app import app

class TestProductEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_add_product1(self):
        payload = {'id': 1, 'name': 'Baseball Cap', 'price': 3.99}
        response = self.app.post('/products', json=payload)
        data = response.get_json()
        if data:
            return 'Test successful!'
        return 'Test failed.'
    
    def test_add_product2(self):
        payload = {'id': 2, 'name': 'T-shirt', 'price': 4.99}
        response = self.app.post('/products', json=payload)
        data = response.get_json()
        if data:
            return 'Test successful!'
        return 'Test failed.'
    
    def test_add_product2(self):
        payload = {'id': 3, 'name': 'Jeans', 'price': 3.99}
        response = self.app.post('/products', json=payload)
        data = response.get_json()
        if data:
            return 'Test successful!'
        return 'Test failed.'
    
if __name__ == '__main__':
    unittest.main()