from django.test import TestCase
from restaurant.models import Menu, Booking
# Create your tests here.

class MenuTest(TestCase):
    def test_get_menu(self):
        item = Menu.objects.create(Title="IceCream", Price=80, Inventory=100)
        self.assertEqual(str(item), "IceCream : $ 80")
