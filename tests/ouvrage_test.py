from main import app
import unittest
from fastapi.testclient import TestClient
from src.schema.ouvrage_schema import OuvrageUpdate

client = TestClient(app)
# pour ne pas répéter dans chaque test, variables des ids :
valid_id_ouvrage = 3
invalid_id_ouvrage = 99999
invalid_ouvrage = {
    "titre_ouvrage": "Titre de l'ouvrage",
    "auteur_ouvrage": "testunitest",
    "isbn_ouvrage": "string",
    "langue_ouvrage": "Breton",
    "prix_ouvrage": 10.0,
    "date_parution_ouvrage": "2023-11-27",
    "categorie_ouvrage": "string",
    "date_disponibilite_libraire_ouvrage": "2023-11-27",
    "date_disponibilite_particulier_ouvrage": "2023-11-27",
    "image_ouvrage": "string",
    "table_des_matieres_ouvrage": "string",
    "mot_cle_ouvrage": "string",
    "description_ouvrage": "string",
}
valid_ouvrage = {
    "titre_ouvrage": "Titre de l'ouvrage",
    "auteur_ouvrage": "testunitest",
    "isbn_ouvrage": "string",
    "langue_ouvrage": "Breton",
    "prix_ouvrage": 10.0,
    "date_parution_ouvrage": "2023-11-27",
    "categorie_ouvrage": "string",
    "date_disponibilite_libraire_ouvrage": "2023-11-27",
    "date_disponibilite_particulier_ouvrage": "2023-11-27",
    "image_ouvrage": "string",
    "table_des_matieres_ouvrage": "string",
    "mot_cle_ouvrage": "string",
    "description_ouvrage": "string",
}


class TestReadOuvrage(unittest.TestCase):
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

    def test_patch_ouvrage_empty(self):
        response = client.patch(
            f"/ouvrages/{valid_id_ouvrage}", json={"titre_ouvrage": ""})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["titre_ouvrage"], "")

    def test_patch_ouvrage_not_found(self):
        # test pour voir avec un invalid id
        response = client.patch(
            f"/ouvrages/{invalid_id_ouvrage}", json={"titre_ouvrage": "Nouveau Titre"})
        self.assertEqual(response.status_code, 404)


class TestPutOuvrage(unittest.TestCase):
    def test_put_ouvrage_success(self):
        response = client.put(
            f"/ouvrages/{valid_id_ouvrage}", json=valid_ouvrage)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        for key in valid_ouvrage.keys():
            self.assertEqual(data[key], valid_ouvrage[key])

    # def test_put_ouvrage_invalid(self):
    #     response = client.put(
    #         f"/ouvrages/{valid_id_ouvrage}", json=invalid_ouvrage)
    #     data = response.json()
    #     for key in valid_ouvrage.keys():
    #         self.assertEqual(data[key], invalid_ouvrage[key])
    #     self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
