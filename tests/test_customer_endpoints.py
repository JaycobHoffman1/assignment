import unittest
from app import app

class TestCustomerEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_add_customer1(self):
        payload = {'id': 1, 'name': 'Jaycob', 'email': 'jaycobhoffman@gmail.com', 'phone': '971-707-1712'}
        response = self.app.post('/customers', json=payload)
        data = response.get_json()
        if data:
            return 'Test successful!'
        return 'Test failed.'
    
    def test_add_customer2(self):
        payload = {'id': 2, 'name': 'Joshua', 'email': 'joshuahoffman@gmail.com', 'phone': '123-456-7890'}
        response = self.app.post('/customers', json=payload)
        data = response.get_json()
        if data:
            return 'Test successful!'
        return 'Test failed.'
    
    def test_add_customer2(self):
        payload = {'id': 3, 'name': 'Cody', 'email': 'codyhoffman@gmail.com', 'phone': '098-765-4321'}
        response = self.app.post('/customers', json=payload)
        data = response.get_json()
        if data:
            return 'Test successful!'
        return 'Test failed.'
    
if __name__ == '__main__':
    unittest.main()