"""Testing the session app"""
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from tests.utils import create_test_user_list


class TestSessionApi(APITestCase):
    """Testing the Api of the sessions app"""

    @classmethod
    def setUpTestData(cls):
        cls.members = create_test_user_list()

    def test_get_sessions(self):
        """Testing get of sessions"""
        url = reverse('api/v1:api-root') + 'session/'
        response = self.client.get(url)
        assert response.status_code == 401
        self.client.login(username='test1@example.com', password='password')
        response = self.client.get(url)
        assert response.status_code == 200

    def test_create_session(self):
        """Testing session creation"""
        url = reverse('api/v1:api-root') + 'session/'
        response = self.client.post(url)
        assert response.status_code == 400
        response = self.client.get(url)
        assert response.status_code == 401
        response = self.client.post(
            url,
            data={
                "email": "test1@example.com",
                "password": "password"
            }
        )
        assert response.status_code == 201
        response = self.client.get(url)
        assert response.status_code == 200

    def test_delete_session(self):
        """Testing the deletion of sessions"""
        url = reverse('api/v1:api-root') + 'session/'
        self.client.login(username='test1@example.com', password='password')
        response = self.client.delete(url)
        assert response.status_code == 200
        response = self.client.get(url)
        assert response.status_code == 401



