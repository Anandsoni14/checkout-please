class ItemInventory:

    def __init__(self):
        self.items = {}

    def add_single_item(self, item: str, rate: int):
        self.items[item] = {
            "base_rate": rate,
            "disc_at_qty": None,
            "special_price": None
        }

    def add_pricing_disc(self, item: str, min_qty: int, price: int):
        if item not in self.items:
            raise "Add Item first"

        self.items[item]["disc_at_qty"] = min_qty
        self.items[item]["special_price"] = price

    def get_regular_price(self, item: str):
        if item not in self.items:
            raise Exception(f"{item} not found in Inventory")
        return self.items[item]['base_rate']

    def get_special_price(self, item: str):
        if item not in self.items:
            raise Exception(f"{item} not found in Inventory")
        return self.items[item]['special_price']

    def get_qty_disc(self, item: str):
        if item not in self.items:
            raise Exception(f"{item} not found in Inventory")
        return self.items[item]['disc_at_qty']