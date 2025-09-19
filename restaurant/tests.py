from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from .models import MenuItem, Booking

User = get_user_model()

class MenuItemModelTest(TestCase):
    def test_menu_item_creation(self):
        item = MenuItem.objects.create(title="Pizza", price=12.5, inventory=10)
        self.assertEqual(item.title, "Pizza")
        self.assertEqual(item.price, 12.5)
        self.assertEqual(item.inventory, 10)

class BookingModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
    def test_booking_creation(self):
        booking = Booking.objects.create(
            name="John Doe", no_of_guests=2,
            booking_date="2025-10-10", booking_time="19:00",
            created_by=self.user
        )
        self.assertEqual(booking.name, "John Doe")
        self.assertEqual(booking.no_of_guests, 2)
        self.assertEqual(booking.created_by, self.user)

class APITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.force_authenticate(user=self.user)

    def test_menu_item_list_create(self):
        url = reverse("menuitem-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        data = {"title": "Burger", "price": 5.99, "inventory": 20}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)

    def test_menu_item_detail_update_delete(self):
        item = MenuItem.objects.create(title="Pasta", price=8.5, inventory=15)
        url = reverse("menuitem-detail", args=[item.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        response = self.client.patch(url, {"price": 9.0})
        self.assertEqual(response.status_code, 200)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)

    def test_booking_list_create(self):
        url = reverse("booking-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        data = {
            "name": "Jane Doe",
            "no_of_guests": 4,
            "booking_date": "2025-10-11",
            "booking_time": "18:30",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)

    def test_booking_detail_update_delete(self):
        booking = Booking.objects.create(
            name="Jane Doe", no_of_guests=4,
            booking_date="2025-10-11", booking_time="18:30",
            created_by=self.user
        )
        url = reverse("booking-detail", args=[booking.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        response = self.client.patch(url, {"no_of_guests": 5})
        self.assertEqual(response.status_code, 200)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)

class AuthTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_register(self):
        url = reverse("user-list")
        data = {"username": "newuser", "password": "newpass123"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)

    def test_login(self):
        User.objects.create_user(username="loginuser", password="loginpass123")
        url = reverse("jwt-create")
        data = {"username": "loginuser", "password": "loginpass123"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("access", response.data)
