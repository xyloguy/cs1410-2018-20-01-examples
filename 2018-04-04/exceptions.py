# d = {}
# key = input('what do you want?')
# if key in d:
#     print(d[key])
# else:
#     print('{} is not in d'.format(key))


# def get_float(a):
#     while True:
#         try:
#             f = float(input(a))
#             return f
#         except ValueError:
#             pass
#
#
# def add(a, b):
#     print(a + b)
#
# while True:
#     a = get_float('first number: ')
#     b = get_float('second number: ')
#     add(a, b)


# def get_item(question, items):
#     a = input(question)
#
#     if len(items) == 0:
#         return None
#
#     try:
#         index = int(a)
#         return items[index]
#     except IndexError:
#         return items[-1]
#     except ValueError:
#         return None
#
# l = [5, 4, 3, 2, 1, 0]
# print(get_item('what index do you want? ', l))
