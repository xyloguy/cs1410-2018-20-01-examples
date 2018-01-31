class Fridge:
    def __init__(self, capacity):
        self.capacity = capacity
        self.inventory = []

    def add_item(self, item):
        removed_item = None
        if len(self.inventory) >= self.capacity:
            # remove the first item
            # del self.inventory[0]
            # self.inventory.pop(0)
            removed_item = self.inventory[0]
            self.inventory = self.inventory[1:]
        self.inventory.append(item)
        return removed_item

    def get_items(self):
        return self.inventory


f = Fridge(3)
if f.add_item('milk') is not None:
    print('An item was removed') # None
print(f.add_item('eggs')) # None
print(f.add_item('bacon')) # None
print(f.add_item('cheese')) # milk


items = ['milk', 'eggs', 'bacon', 'cheese', 'juice', 'red bull']
for item in items:
    removed_item = f.add_item(item)
    if removed_item is not None:
        print('Removed', removed_item)
