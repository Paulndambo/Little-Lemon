from django.test import TestCase
from restaurant.models import Menu


class MenuTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Ice", price=800, inventory=100)
        Menu.objects.create(title="Cream", price=8, inventory=100)

    def test_getall(self):
        ice = Menu.objects.get(title="Ice")
        cream = Menu.objects.get(title="Cream")
        self.assertEqual(str(ice), "Ice : 800.00")
        self.assertEqual(str(cream), "Cream : 8.00")
