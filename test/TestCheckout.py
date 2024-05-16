import unittest
from unittest.mock import patch
from src.Checkout import Checkout
from src.ItemInventory import ItemInventory
from src.Utils import Utils


class TestCheckout(unittest.TestCase):

    def setUp(self):
        self.utils = Utils()
        self.inventory = ItemInventory()
        self.inventory.add_single_item("A", 50)
        self.inventory.add_pricing_disc("A", 3, 130)
        self.inventory.add_single_item("B", 30)
        self.inventory.add_pricing_disc("B", 2, 45)
        self.inventory.add_single_item("C", 20)
        self.inventory.add_single_item("D", 15)
        self.checkout = Checkout(self.inventory)

    @patch('builtins.input', lambda *args: 'AAABBBCCCD')
    def test_add_item_to_bill(self):
        self.checkout.add_item_to_bill()
        self.assertEqual(self.checkout.billed_items, 'AAABBBCCCD')

    def test_per_item_total_price(self):
        total_price = self.checkout.per_item_total_price("A", 5)
        self.assertEqual(total_price, 230)  # 3 A's at special price (130) + 2 A's at regular price (50*2)

        total_price = self.checkout.per_item_total_price("B", 4)
        self.assertEqual(total_price, 90)  # 2 sets of 2 B's at special price (45 * 2)

        total_price = self.checkout.per_item_total_price("C", 2)
        self.assertEqual(total_price, 40)  # 2 C's at regular price (20 * 2)

        total_price = self.checkout.per_item_total_price("D", 1)
        self.assertEqual(total_price, 15)  # 1 D at regular price (15)

        total_price = self.checkout.per_item_total_price("E", 5)
        self.assertEqual(total_price, 0)  # E is not in inventory

    def test_bill_please(self):
        self.checkout.billed_items = 'AAABBBCCCD'
        bill_total = self.checkout.bill_please()
        expected_total = 280
        self.assertEqual(bill_total, expected_total)

    def test_validate_billed_items(self):
        # Valid cases
        self.assertTrue(self.utils.validate_billed_items("ABCD", self.inventory))
        self.assertTrue(self.utils.validate_billed_items("AABBCCDD", self.inventory))

        # Invalid cases: contains numbers
        self.assertEqual(self.utils.validate_billed_items("A1BCD", self.inventory),
                         "Invalid character, please check the input")
        self.assertEqual(self.utils.validate_billed_items("1234", self.inventory),
                         "Invalid character, please check the input")

        # Invalid cases: contains spaces
        self.assertEqual(self.utils.validate_billed_items("A BCD", self.inventory),
                         "Invalid character, please check the input")
        self.assertEqual(self.utils.validate_billed_items(" ", self.inventory),
                         "Invalid character, please check the input")

        # Invalid cases: non-existing items
        self.assertEqual(self.utils.validate_billed_items("ABCDE", self.inventory), "Item E not found")
        self.assertEqual(self.utils.validate_billed_items("XYZ", self.inventory), "Item X not found")

    def test_checkout_with_inputs(self):
        test_cases = [
            ("", 0),
            ("A", 50),
            ("AB", 80),
            ("CDBA", 115),
            ("AA", 100),
            ("AAA", 130),
            ("AAAA", 180),
            ("AAAAA", 230),
            ("AAAAAA", 260),
            ("AAAB", 160),
            ("AAABB", 175),
            ("AAABBD", 190),
            ("DABABA", 190),
            ("DAB ABA", "Invalid character, please check the input"),
            ("DA1ABA", "Invalid character, please check the input"),
            ("DAEABA", "Item E not found")

        ]

        for items, expected_total in test_cases:
            self.checkout.billed_items = items
            self.assertEqual(self.checkout.bill_please(), expected_total)


if __name__ == '__main__':
    unittest.main()
