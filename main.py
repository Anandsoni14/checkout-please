from src.Checkout import Checkout
from src.ItemInventory import ItemInventory


def setup_inventory():
    inventory = ItemInventory()

    inventory.add_single_item('A', 50)
    inventory.add_pricing_disc('A', 3, 130)

    inventory.add_single_item('B', 30)
    inventory.add_pricing_disc('B', 2, 45)

    inventory.add_single_item('C', 20)

    inventory.add_single_item('D', 15)

    return inventory


if __name__ == '__main__':
    avail = setup_inventory()
    checkout = Checkout(avail)

    checkout.add_item_to_bill()
    total_bill = checkout.bill_please()
    if type(total_bill) is int:
        print(f"Please pay Rs.{total_bill}")
    else:
        print(total_bill)




