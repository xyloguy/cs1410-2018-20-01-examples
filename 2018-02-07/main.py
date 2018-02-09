def a():
    return 'calling a'

def b():
    return 'calling b'

def c():
    return 'calling c'



d = {
    'a': a,
    'b': b,
    'c': c,
}

ask = input('a, b, or c? ')
print(d[ask]())

