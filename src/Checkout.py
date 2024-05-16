from src.ItemInventory import ItemInventory
from src.Utils import Utils
from collections import Counter


class Checkout:

    def __init__(self, inventory: ItemInventory):
        self.billed_items = ""
        self.inventory = inventory

    def add_item_to_bill(self):
        self.billed_items = input("Add Items: ")
        print(f"Please pay Rs.{self.bill_please()}")
        return

    def per_item_total_price(self, item: str, total_qty: int):
        discounted_item_price = 0
        regular_item_price = 0
        item_inventory = self.inventory
        # print(item_inventory.items)
        if item not in item_inventory.items:
            return 0

        min_qty = item_inventory.get_qty_disc(item)
        special_price = item_inventory.get_special_price(item)
        regular_price = item_inventory.get_regular_price(item)

        if min_qty is None or special_price is None:
            regular_item_price = total_qty * regular_price
        else:
            discounted_qty = (total_qty // min_qty) if min_qty else 0
            discounted_item_price = discounted_qty * special_price

            regular_qty = (total_qty % min_qty) if min_qty else total_qty
            regular_item_price = regular_qty * regular_price

        return discounted_item_price + regular_item_price

    def bill_please(self):
        utils = Utils()

        is_items_validate = utils.validate_billed_items(self.billed_items, self.inventory)

        if is_items_validate is not True:
            return is_items_validate

        items_count = Counter(self.billed_items)
        # print(items_count)
        bill_total = sum(self.per_item_total_price(item, qty) for item, qty in items_count.items())

        return bill_total
