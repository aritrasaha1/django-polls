import unittest
from unittest.mock import patch, MagicMock
from django.urls import reverse
from django.test import TestCase
from wrap_app.views import spotify_login


class SpotifyLoginTests(TestCase):
    
    @patch('wrap_app.views.requests.post')  # Mock the requests.post method
    def test_spotify_login_success(self, mock_post):
        """
        Test successful Spotify login flow.
        """
        # Mock the response from Spotify
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'access_token': 'mock_token', 'user_id': 'mock_user'}
        mock_post.return_value = mock_response
        
        # Simulate a GET request to the spotify login
        response = self.client.get(reverse('wrap_app:spotify_login', kwargs={'action': 'connect_spotify'}))
        
        # Check if the response redirects correctly
        self.assertEqual(response.status_code, 302)  # Should redirect after successful login
        self.assertRedirects(response, '/en/dashboard/')  # Ensure it redirects to the dashboard
        
        # Check that the Spotify connection happened
        self.assertIn('mock_user', response.content.decode())  # Ensure the user ID is passed into the page

    @patch('wrap_app.views.requests.post')
    def test_spotify_login_failure(self, mock_post):
        """
        Test Spotify login failure (e.g., bad token exchange).
        """
        # Mock a failed response from Spotify
        mock_response = MagicMock()
        mock_response.status_code = 400  # Bad Request
        mock_post.return_value = mock_response
        
        response = self.client.get(reverse('wrap_app:spotify_login', kwargs={'action': 'connect_spotify'}))
        
        # Ensure the failure redirects to the home page with an error message
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/en/home/')
        self.assertContains(response, "Failed to authenticate with Spotify.")
