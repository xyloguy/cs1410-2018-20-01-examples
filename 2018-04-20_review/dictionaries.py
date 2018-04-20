# Create a dictionary
d = {}
d2 = dict()

# Add item into dictionary
d[0] = 'this'
d['0'] = 'that'
d[(0, 0)] = 'wat'
print(d)


# Update existing item
d[0] = 'changed'
print(d)


# check if key in dictionary
key = 'blah'
if key in d:
    print('its there')
else:
    print(key, 'not in dictionary')


# check if value in dictionary
word = 'that'
found = False
for key in d:
    if d[key] == word:
        print('its there')
        found = True
        break
if not found:
    print(word, 'not in dictionary')

# option 2
if word in d.values():
    print('its there')
else:
    print(word, 'not in dictionary')


def foo():
    return 'foo'

def bar():
    return 'bar'

def foobar():
    return foo() + bar()


functions = {
    'a': foo,
    'b': bar,
    'c': foobar
}

while True:
    a = input('press a key')
    if a in functions:
        print(functions[a]())
        break

    print(a, 'is not a valid option')


