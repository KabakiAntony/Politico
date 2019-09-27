# tests from the office views.
import unittest
import json
from app import create_app
from app.api.v1.models.Office import OFFICE

class TestOfficeViews(unittest.TestCase):


    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.test_office = {
            "name": "test office",
            "office_type": "test type"
            }
        self.invalid_office = {
            "id_":1
            }
        self.specific_office = {
            "id":0,
            "name": "test office",
            "office_type": "test type"
            }
        self.updated_office = {
            "name":"new office"
        }
    

    def tearDown(self):
        self.app.testing = False

    def post(self,data={}):
        """ This is just a helper method for the 
        test cases that need to post data see
        comments for more explanation."""
        if not data:
            data = self.test_office
        response = self.client.post(
            'api/v1/offices',data=json.dumps(self.test_office), content_type='application/json')
        return response


    def test_creating_office(self):
        """Test creation of an office """
        response = self.post()
        self.assertEqual(response.status_code,201)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result["Data"], self.specific_office)
        self.assertEqual(result["Status"], 201)