import item


class Backpack:
    def __init__(self, capacity):
        self.items = []
        self.capacity = capacity

    def set_item(self, item):
        if len(self.items) < self.capacity:
            self.items.append(item)
            return True
        return False

    def get_name(self):
        s = ''
        for thisitem in self.items:
            s += thisitem.get_name()
            s += ' '
        if s != '':
            return s
        return 'No items'

    def get_value(self):
        total = 0.0
        for thisitem in self.items:
            total += thisitem.get_value()
        return total

i = item.Item('Pen', 0.05)
bag = Backpack(5)
print(bag.get_value())
print(bag.get_name())

items = [
    item.Item('Pen', 0.05),
    item.Item('Pencil', 0.03),
    item.Item('Notebook', 0.88),
    item.Item('Notebook', 0.88),
    item.Item('Calculator', 80.00),
    item.Item('Binder', 2.50),
    item.Item('Eraser', 0.35),
]

for i in items:
    if not bag.set_item(i):
        print(i.get_name(), 'could not be added')
    else:
        print(i.get_name(), 'was added')

print(bag.get_value())
print(bag.get_name())