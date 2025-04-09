# test_app.py
import unittest
import json
import sys

sys.path.append("../")
from app import app 

class TestAPI(unittest.TestCase):
    id = None
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        

    def tearDown(self):
        pass

    def test_create_recipt(self):
        
        recipt = {
                "retailer": "M&M Corner Market",
                "purchaseDate": "2022-03-20",
                "purchaseTime": "14:33",
                "items": [
                    {
                    "shortDescription": "Gatorade",
                    "price": "2.25"
                    },{
                    "shortDescription": "Gatorade",
                    "price": "2.25"
                    },{
                    "shortDescription": "Gatorade",
                    "price": "2.25"
                    },{
                    "shortDescription": "Gatorade",
                    "price": "2.25"
                    }
                ],
                "total": "9.00"
        }
        response = self.app.post('/receipts/process', json=recipt)
        data = response.get_json()
        self.assertIn("id", data, f"Key 'id' should be in the dictionary")
       
        #save the id 
        TestAPI.id = data["id"]



    def test_get_points(self):
        self.assertEqual('Hello, world!', 'Hello, world!')
        response = self.app.get('/receipts/'+str(TestAPI.id)+'/points')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["points"], 109)

if __name__ == '__main__':
    unittest.main()