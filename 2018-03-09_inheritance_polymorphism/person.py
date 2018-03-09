class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name + ' ' + self.pay_bills() + ' ' + self.eat_dinner()

    def pay_bills(self):
        return "Don't forget uncle sam's share"

    def eat_dinner(self):
        raise NotImplementedError('You need to implement this on a child class')


class MyPerson(Person):
    def eat_dinner(self):
        return "I'll have Pizza"


class Student(Person):
    def __init__(self, name, age, sid):
        Person.__init__(self, name, age)
        self.sid = sid
        self.debt = 0

    def add_debt(self, debt):
        self.debt += debt

    def pay_bills(self):
        return 'Mom'

    def eat_dinner(self):
        return 'That activity has free food'

p = Student('John', 30, '10001000')
p.add_debt(1000)
print(p.debt)
print(p.pay_bills())
print(p.eat_dinner())
print(p)
