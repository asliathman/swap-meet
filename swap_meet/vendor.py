from .item import Item

class Vendor:
    def __init__(self, inventory=None):
        if inventory:
            self.inventory = inventory
        else:
            self.inventory = []

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_category(self, category):
        items_by_category = []
        for item in self.inventory:
            if item.category == category:
                items_by_category.append(item)

        return items_by_category

    def swap_items(self, friend, my_item, their_item):

        if my_item in self.inventory and their_item in friend.inventory:
            self.inventory.remove(my_item)
            friend.inventory.remove(their_item)
            friend.inventory.append(my_item)
            self.inventory.append(their_item)
            return True
        else:
            return False

    def swap_first_item(self, friend):
        if self.inventory and friend.inventory:
            return self.swap_items(friend, self.inventory[0], friend.inventory[0])
        else:
            return False
    
    def get_best_by_category(self, category):
        inventory = self.inventory
        decending_condition_inventory = sorted(inventory, key=lambda item: item.condition, reverse=True)


        for item in decending_condition_inventory:
            if item.category == category:
                return item
        
        return None

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_swap = self.get_best_by_category(their_priority)
        their_swap = other.get_best_by_category(my_priority)
        
        if my_swap and their_swap:
            return self.swap_items(other, my_swap, their_swap)
        else:
            return False
