import json 
import unittest
from app import create_app
from app.api.v1.models.Party import Party,PARTY


class TestPartyViews(unittest.TestCase):
    
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.test_party = {
            "name": "test name",
            "hqAddress": "test address",
            "logoUrl": "test url"
            }
        self.specific_party = {
            "id":0,
            "name": "test name",
            "hqAddress": "test address",
            "logoUrl": "test url"
            }
        self.updated_party = {
            "name": "updated name"
            }
    

    def tearDown(self):
        self.app.testing = False
    

    def create(self,data={}):
        """ This is just a helper method for the 
        test cases that need to post data see
        comments in the office module for more explanation."""
        if not data:
            data = self.test_party
        response = self.client.post(
            'api/v1/parties',data=json.dumps(self.test_party), content_type='application/json')
        return response
    

    def test_creating_party(self):
        """ Test the creation of a party """
        response = self.create()
        self.assertEqual(response.status_code,201)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result["Data"], self.specific_party)
        self.assertEqual(result["Status"], 201)
    
    def test_getting_all_parties(self):
        """Test getting all parties """
        #self.create()
        response = self.client.get('api/v1/parties')
        self.assertEqual(response.status_code,200)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result["Data"], [self.specific_party])
        self.assertEqual(result["Status"], 200)

    
    def test_getting_specific_party(self):
        """Test getting a specific party"""
        response = self.client.get('api/v1/parties/{}'.format(0))
        self.assertEqual(response.status_code,200)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result["Data"], [self.specific_party])
        self.assertEqual(result["Status"], 200)
        