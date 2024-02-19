from django.test import TestCase
from restaurant.models import MenuItem


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(
            title="Example",
            price=15.99,
            inventory=4
        )
        self.assertEqual(item, "Example : 15.99")