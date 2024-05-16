from src.ItemInventory import ItemInventory
import re


class Utils:

    def __init__(self):
        self.empty = None

    def validate_billed_items(self, items, inventory: ItemInventory):
        if re.search(r'[0-9\W]', items):
            return "Invalid character, please check the input"

        # Check if every item exists in the inventory
        for item in items:
            if item not in inventory.items:
                return f"Item {item} not found"

        return True
