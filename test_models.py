import pytest
from django.contrib.auth import get_user_model
from django.test import TestCase

# Adjust import below to your actual models
# from .models import Reservation

User = get_user_model()

class ReservationModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        # Uncomment and adjust below when Reservation model is available
        # self.reservation = Reservation.objects.create(
        #     name="John Doe",
        #     guests=2,
        #     reservation_time="2025-10-10 19:00",
        #     user=self.user
        # )

    def test_user_creation(self):
        assert self.user.username == "testuser"

    # Example model test - adjust to your models
    # def test_reservation_str(self):
    #     assert str(self.reservation) == "Reservation for John Doe at 2025-10-10 19:00"