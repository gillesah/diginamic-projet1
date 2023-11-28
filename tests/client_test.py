from main import app
import unittest
from fastapi import status
from fastapi.testclient import TestClient

# cmd line to start the test: python -m unittest tests/client_test.py

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
    
class TestPatchClient(unittest.TestCase):

    def test_patch_client_success(self):
        response = client.patch(f"/client/{valid_id_client}", json={"nom_client": "(§è!çàç!è§((§è!ç)))"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data["nom_client"], "(§è!çàç!è§((§è!ç)))")

    def test_patch_client_empty(self):
        response = client.patch(f"/client/{valid_id_client}", json={"nom_client": ""})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data["nom_client"], "")

    def test_patch_client_not_found(self):
        # test with an invalid id client
        response = client.patch(f"/client/{invalid_id_client}", json={"nom_client": "nomclient"})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        