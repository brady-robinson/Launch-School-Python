# def greet_all(*names):
#     print(names)
#     for name in names:
#         print(name)

# greet_all('chris', 'pete', 'nick')

# def greet_all(**names):
#     print(names)
#     for name in names:
#         print(name)

# greet_all(christopher='chris', peter='pete', nicholas='nick')

# def combine(a, b, c):
#     return (a, b, c)

# print(combine(1, 2, 3))

# def multiply(a, b, /):
#     return a * b

# print(multiply(1, b=2))

# def describe_pet(animal_type, *, name=''):
#     print(f'{name} is a {animal_type}')

# describe_pet('dog', name='doggy')
# describe_pet('dog', 'cat', name='doggy')

# def calculate_average(*args):
#     len_args = len(args)

#     if len_args == 0:
#         return None
    
#     sum_args = sum(args)

#     return sum_args / len_args

# print(calculate_average(1, 2, 3, 4))      # 2.5

# def find_person(**kwargs):
#     for key, val in kwargs:
#         if key == 'Antonina':
#             print(f'{key} is a {val}')

# def concat_strings(*args, sep=' '):
#     return sep.join(args)

# def register(username, /, age=None, *, password):
#     pass

def print_message(*, message, level='INFO'):
    print(f"{level}{message}")