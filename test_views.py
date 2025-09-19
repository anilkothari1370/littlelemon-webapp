import pytest
from django.urls import reverse
from django.test import Client, TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class ReservationViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.login(username="testuser", password="testpass")

    def test_home_page(self):
        url = reverse("home")  # Replace "home" with your actual view name
        response = self.client.get(url)
        assert response.status_code == 200

    
     def test_reservation_list_view(self):
        url = reverse("reservation-list")
        response = self.client.get(url)
        assert response.status_code == 200
