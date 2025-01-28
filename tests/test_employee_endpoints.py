import unittest
from app import app

class TestEmployeeEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_add_employee1(self):
        payload = {'id': 1, 'name': 'Jaycob', 'position': 'Senior Developer'}
        response = self.app.post('/employees', json=payload)
        data = response.get_json()
        if data:
            return 'Test successful!'
        return 'Test failed.'
    
    def test_add_employee2(self):
        payload = {'id': 2, 'name': 'Joshua', 'position': 'CEO'}
        response = self.app.post('/employees', json=payload)
        data = response.get_json()
        if data:
            return 'Test successful!'
        return 'Test failed.'
    
    def test_add_employee2(self):
        payload = {'id': 3, 'name': 'Cody', 'position': 'Vice President'}
        response = self.app.post('/employees', json=payload)
        data = response.get_json()
        if data:
            return 'Test successful!'
        return 'Test failed.'
    
if __name__ == '__main__':
    unittest.main()