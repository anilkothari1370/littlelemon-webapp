import pytest
from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Reservation

User = get_user_model()

class ReservationModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.reservation = Reservation.objects.create(
            name="John Doe",
            guests=2,
            reservation_time="2025-10-10 19:00",
            user=self.user
        )

    def test_user_creation(self):
        assert self.user.username == "testuser"

    def test_reservation_str(self):
        expected_str = "Reservation for John Doe at 2025-10-10 19:00"
        assert str(self.reservation) == expected_str

    def test_reservation_guest_count(self):
        assert self.reservation.guests == 2

    def test_reservation_time(self):
        assert str(self.reservation.reservation_time) == "2025-10-10 19:00:00"

    def test_reservation_user(self):
        assert self.reservation.user == self.user
