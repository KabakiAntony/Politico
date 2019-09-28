import json 
import unittest
from app import create_app
from app.api.v1.models import Party,PARTY


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
        