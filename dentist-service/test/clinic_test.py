import unittest
from flask import Flask

class ClinicRoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.client = self.app.test_client()

    def test_add_clinic(self):
        data = {
            "name": "Test Clinic",
            "address": "Test St. Test",
            "location": {
                "latitude": 59.340688797415794,
                "longitude": 18.06328148314156
            }
        }

        response = self.client.post('/clinics/', json=data)
        self.assertEqual(response.status_code, 201)

    def test_get_clinics(self):
        response = self.client.get('/clinics/')
        self.assertEqual(response.status_code, 200)

    def test_get_single_clinic(self):
        clinic_id = "Test Clinic"
        response = self.client.get(f'/clinics/{clinic_id}')
        self.assertIn(response.status_code, [200, 404])

    def test_update_clinic(self):
        clinic_id = "Test Clinic"
        data = {"name": "Updated Clinic Name"}
        response = self.client.put(f'/clinics/{clinic_id}', json=data)
        self.assertIn(response.status_code, [200, 404])

    def test_delete_clinic(self):

        clinic_id = "Test Clinic"
        response = self.client.delete(f'/clinics/{clinic_id}')
        self.assertIn(response.status_code, [204, 404])

if __name__ == '__main__':
    unittest.main()
