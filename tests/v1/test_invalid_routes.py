import json 
import unittest
from app import create_app

class TestInvalidRoutes(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def tearDown(self):
        self.app.testing = False

    def test_getting_invalid_route(self):
        """Test getting invalid routes"""
        response = self.client.get('api/v1/parties/')
        self.assertEqual(response.status_code,404)
        response = self.client.get('api/v1/anything')
        self.assertEqual(response.status_code,404)
