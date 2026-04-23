import unittest
from app import app

class TestServer(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_health_check(self):
        response = self.app.get('/test')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['status'], 'ok')

    def test_enhance_requires_text(self):
        response = self.app.post('/enhance', json={})
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()