from main import app
import unittest
from fastapi.testclient import TestClient
from src.schema.ouvrage_schema import OuvrageUpdate

client = TestClient(app)
# pour ne pas répéter dans chaque test, variables des ids :
valid_id_ouvrage = 3
invalid_id_ouvrage = 99999


class TestReadOuvrage(unittest.TestCase):
    # def setUp(self):
    #     self.client = TestClient(app)

    def test_read_ouvrage_success(self):
        # id normalement valide
        response = client.get(f"/ouvrages/{valid_id_ouvrage}")
        self.assertEqual(response.status_code, 200)

    def test_read_ouvrage_not_found(self):
        # id peu probable d'exister
        response = client.get(f"/ouvrages/{invalid_id_ouvrage }")
        self.assertEqual(response.status_code, 404)


class TestPatchOuvrage(unittest.TestCase):

    def test_patch_ouvrage_success(self):
        response = client.patch(
            f"/ouvrages/{valid_id_ouvrage}", json={"titre_ouvrage": "(§è!çàç!è§((§è!ç)))"})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["titre_ouvrage"], "(§è!çàç!è§((§è!ç)))")

    def test_patch_ouvrage_not_found(self):
        # test pour voir avec un invalid id
        response = client.patch(
            f"/ouvrages/{invalid_id_ouvrage}", json={"titre_ouvrage": "Nouveau Titre"})
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
