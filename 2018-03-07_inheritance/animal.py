class Animal:
    def speak(self):
        return 'Animals do not speak'


class Dog(Animal):
    def speak(self):
        return 'Woof'


class Cat(Animal):
    def speak(self):
        return 'Meow'


class Fox(Animal):
    def speak(self):
        return 'Error'


animals = [Animal(), Dog(), Cat(), Fox()]
for animal in animals:
    print(animal.speak())

