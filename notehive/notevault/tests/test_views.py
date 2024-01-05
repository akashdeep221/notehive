# TODO: has to fix bugs


from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from notehive.notevault.models import Note

#from notehive.notevault.models import Note

class NoteViewsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)

    def test_note_list_create_view(self):
        response = self.client.get('/api/notes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = {'title': 'Test Note', 'content': 'Test Content'}
        response = self.client.post('/api/notes/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_note_detail_view(self):
        note = Note.objects.create(title='Test Title', content='Test Content', owner=self.user)
        response = self.client.get(f'/api/notes/{note.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_note_search_view(self):
        response = self.client.get('/api/search/?q=test')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_signup_view(self):
        data = {'username': 'newuser', 'password': 'newpass'}
        response = self.client.post('/api/auth/signup/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login_view(self):
        data = {'username': 'testuser', 'password': 'testpass'}
        response = self.client.post('/api/auth/login/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)
