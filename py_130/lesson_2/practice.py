# lst = [1, 2, 3]

# # print(list(map(lambda x: x**2, lst)))

# # def even_num(x):
# #     return x % 2 == 0

# # print(list(filter(even_num, lst)))

# from functools import reduce

# def multiply(x, y):
#     return x * y

# print(reduce(multiply, lst))

# lst = [None, 'hello', 'hey']

# def get_length(string):
#     return len(string)

# lengths = map(get_length, lst)
# print(list(lengths))

# def not_none(arg):
#     return arg is not None

# print(list(filter(lambda x: x is not None, lst)))

# lst = ['hello', 'hey']

# from functools import reduce

# all_string = reduce(lambda x, y: x + y, lst)
# print(all_string)

# nested_lists = [[1, 2, 3], [4, 5], [6]]

# gen = (num for sub_list in nested_lists for num in sub_list)

# for num in gen:
#     print(num)

# string = 'hello'

# rev_strings = (char for char in reversed(string))

# for char in rev_strings:
#     print(char)

# def num_gen():
#     for i in range(1, 6):
#         yield i

# for num in num_gen():
#     print(num)

# def greet(name, greeting, punc='.'):
#     return f"{greeting}, {name}{punc}"

# print(greet("Antonina", "Hello")) # Hello, Antonina.
# print(greet("Pete", "Good morning", "!")) # Good Morning, Pete!

# def create_user(username,*, email, age):
#     return {'username':username, 'email':email, 'age':age}

# print(create_user("Srdjan", email="srdjan@example.com", age=39))
# # {"username": "Srdjan", "email": "srdjan@example.com", "age": 39}
# print(create_user("Srdjan", "srdjan@example.com", age=39))
# # Raises an exception

# def build_profile(first_name, last_name, **kwargs):
#     output = {'first_name':first_name, 'last_name':last_name}
#     for key, value in kwargs.items():
#         output[key] = value

#     return output

# print(build_profile("Max", "Hawkins", location="San Francisco", field="Software Engineering"))
# # {'first_name': 'Max', 'last_name': 'Hawkins', 'location': 'San Francisco', 'field': 'Software Engineering'}

# def concatenate(*args):
#     return ' '.join(args)

# print(concatenate("Launch", "School", "is", "great")) # Launch School is great
# print(concatenate("I", "am", "working", "on", "the", "PY130", "course")) # I am working on the PY130 course

# def display_info(data, /, *, reverse=False, uppercase=False):
    
#     if uppercase:
#         data = data.upper()

#     if reverse:
#         data = list(data)
#         data.reverse()
#         data = ''.join(data)

#     return data

# print(display_info("Launch", reverse=True)) # hcnuaL
# print(display_info("School", uppercase=True)) # SCHOOL
# print(display_info("cat", uppercase=True, reverse=True)) # TAC

# data = (100, 200, 300, 400)
# first, *_, last = data

# print(first, last)

# numbers = [1, 2, 3, 4, 5, 6]
# first, second, *rest = numbers

# data = ((1, 2), (3, 4), (5, 6))
# (one, two), (three, four), (five, six) = data