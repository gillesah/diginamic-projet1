from main import app
import unittest
from fastapi import status
from fastapi.testclient import TestClient

client = TestClient(app)
valid_id_client = 2
invalid_id_client = 99999

class TestReadClient(unittest.TestCase):
    def test_read_client_success(self):
        # the id client is valid
        response = client.get(f"/client/{valid_id_client}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_client_not_found(self):
        # the id client is not valid
        response = client.get(f"/client/{invalid_id_client}")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        