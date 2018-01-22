import random


def read_things():
    file = open('things.txt', 'r')
    words = []
    for line in file:
        line = line.strip()
        words.append(line)
    return words


def read_descriptors():
    file = open('descriptors.txt', 'r')
    words = file.readline().strip()
    words = words.split(',')
    return words


def number():
    n = random.randrange(1, 100)
    n = str(n)
    if len(n) < 2:
        n = '0' + n
    return n


def choice(l):
    i = random.randrange(len(l))
    return l[i]


def password():
    descriptor = random.choice(read_descriptors())
    thing = random.choice(read_things())
    num = number()
    return descriptor + thing + num


for i in range(10):
    print(password())

s = 'Hello, World'
print(s[random.randrange(2)::2])
