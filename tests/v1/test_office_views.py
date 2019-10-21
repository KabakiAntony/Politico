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

    # the reason am posting in test_getting_all_offices is
    # because tests are run alphabetically in
    # the test module hence delete runs before get
    # so I have to create my data again before getting 
    # it since it has already being deleted

    def test_getting_all_offices(self):
        """Test getting all offices """
        self.post()
        response = self.client.get('api/v1/offices')
        self.assertEqual(response.status_code,200)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result["Data"], [self.specific_office])
        self.assertEqual(result["Status"],200)

    def test_getting_specific_office(self):
        """Test getting a specific office """
        response = self.client.get('api/v1/offices/{}'.format(0))
        self.assertEqual(response.status_code,200)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result["Data"], self.specific_office)
        self.assertEqual(result["Status"],200)

    def test_getting_a_non_existent_office(self):
        """Test getting a non-existent office"""
        response = self.client.get('api/v1/offices/{}'.format(20))
        self.assertEqual(response.status_code,404)


    def test_deleting_office(self):
        """ Test deletion of an office """
        # delete may or may not have a body so in this case it does not 
        # hence no content type header
        response = self.client.delete('api/v1/offices/{}'.format(0))
        self.assertEqual(response.status_code,200)
    
    
    def test_deleting_a_non_existent_office(self):
        """ Test deleting a non-existent office """
        response = self.client.delete('api/v1/offices/{}'.format(1000))
        self.assertEqual(response.status_code,404)

    

    def test_updating_office(self):
        """Test updating an office """
        response = self.client.patch('api/v1/offices/{}/name'.format(0),
            data=json.dumps(self.updated_office),content_type='application/json')
        self.assertEqual(response.status_code,200)


    def test_updating_a_non_existent_toffice(self):
        """Test updating a non-existent office """
        response = self.client.patch('api/v1/offices/{}/name'.format(100),
            data=json.dumps(self.updated_office),content_type='application/json')
        self.assertEqual(response.status_code,404)