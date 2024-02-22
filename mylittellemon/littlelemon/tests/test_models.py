from django.test import TestCase
from restaurant.models import Menu


class MenuTest(TestCase):
    def  test_get_item(self):
        item = Menu.objects.create(Title="Pizza", Price=10.00, Inventory=33)
        self.assertEqual(item.Title, "Pizza")
        self.assertEqual(item.Price, 10.00)
        self.assertEqual(item.Inventory, 33)
        
