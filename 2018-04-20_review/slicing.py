# slicing
# string[start:end:step]


a = "Hello, World!"


# get "He"
print(a[:2])


# Odd Indexed Chars
print(a[1::2])


# Reverse a string
print(a[::-1])  # beginning to the end, stepping backwards

# Reverse using for loop
b = ''
for i in range(0, len(a)):
    index = len(a) - 1 - i
    b += a[index]
print(b)

def string_contains(string, word):
    for char in word.upper():
        if char not in string.upper():
            return False
    return True

a = "Hello, World!"
print(string_contains(a, 'He')) # True
print(string_contains(a, 'he')) # False
