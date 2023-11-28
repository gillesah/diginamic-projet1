from main import app
import unittest
from fastapi import status
from fastapi.testclient import TestClient

# cmd line to start the test: python -m unittest tests/client_test.py

client = TestClient(app)
valid_id_client = 2
invalid_id_client = 99999
valid_client = {
    "nom_client": "nom_client",
    "prenom_client": "prenom_client",
    "email_client": "email_client",
    "telephone_client": "telephone_client",
    "preferences_client": "preferences_client",
    "adresse_livraison_client": "adresse_livraison_client",
    "adresse_facturation_client": "adresse_facturation_client"
}

invalid_client = {
    "nom_client": "",
    "prenom_client": "",
    "email_client": "",
    "telephone_client": "telephone_client",
    "preferences_client": "preferences_client",
    "adresse_livraison_client": "adresse_livraison_client",
    "adresse_facturation_client": "adresse_facturation_client"
}

class TestReadClient(unittest.TestCase):
    def test_read_client_success(self):
        # test to read with a valid id client
        response = client.get(f"/client/{valid_id_client}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_client_not_found(self):
        # test to read with an invalid id client
        response = client.get(f"/client/{invalid_id_client}")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
class TestPatchClient(unittest.TestCase):

    def test_patch_client_success(self):
        # test with a valid client id and a lot of special caracters
        response = client.patch(f"/client/{valid_id_client}", json={"nom_client": "(§è!çàç!è§((§è!ç)))"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data["nom_client"], "(§è!çàç!è§((§è!ç)))")

    def test_patch_client_empty(self):
        # test with a valid client id and an empty client name
        response = client.patch(f"/client/{valid_id_client}", json={"nom_client": ""})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data["nom_client"], "")

    def test_patch_client_not_found(self):
        # test with an invalid id client
        response = client.patch(f"/client/{invalid_id_client}", json={"nom_client": "nomclient"})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
        
class TestPutClient(unittest.TestCase):
    def test_put_client_success(self):
        response = client.put(f"/client/{valid_id_client}", json=valid_client)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        for key in valid_client.keys():
            self.assertEqual(data[key], valid_client[key])

    # def test_put_client_invalid(self):
    #     response = client.put(f"/client/{valid_id_client}", json=invalid_client)
    #     data = response.json()
    #     for key in valid_client.keys():
    #         self.assertEqual(data[key], invalid_client[key])
    #     self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        