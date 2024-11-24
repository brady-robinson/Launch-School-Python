# nums = [1, 2, 3, 4]
# sq_nums = [n**2 for n in nums]
# print(sq_nums)

# even_nums = [n for n in nums if n % 2 == 0]
# print(even_nums)

# sq_even_nums = [n**2 for n in nums if n % 2 == 0]
# print(sq_even_nums)

# fruits = ['apple', 'banana', 'cherry']
# dict_fruit = {f:len(f) for f in fruits if f[0] in 'ac'}
# print(dict_fruit)

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8]
# ]

# flat_mat = [num for row in matrix
#                 if len(row) < 3
#                 for num in row
#                 if num > 7]

# print(flat_mat)

# munsters = {
#     'Herman':  {'age': 32,  'gender': 'male'},
#     'Lily':    {'age': 30,  'gender': 'female'},
#     'Grandpa': {'age': 402, 'gender': 'male'},
#     'Eddie':   {'age': 10,  'gender': 'male'},
#     'Marilyn': {'age': 23,  'gender': 'female'},
# }

# ages = [munsters[key]['age'] for key in munsters if munsters[key]['gender'] == 'male']
# print(sum(ages))

# lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

# sorted_lst = [sorted(el) for el in lst]

# sorted_lst = [sorted(el, key=str) for el in lst]
# print(sorted_lst)

# lst = [
#     ['a', 1],
#     ['b', 'two'],
#     ['sea', {'c': 3}],
#     ['D', ['a', 'b', 'c']]
# ]

# dict_lst = {el[0]: el[1] for el in lst}
# print(dict_lst)

# def sort_lst(lst):
#     return sum([n for n in lst if n % 2 != 0])

# lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]
# sorted_lst = sorted(lst, key=sort_lst)
# print(sorted_lst)

# lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

# def increment_values(item):
#     return {key: value + 1 for key, value in item.items()}

# new_lst = [increment_values(el) for el in lst]
# print(new_lst)

# lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

# def divisible_by_3(lst):
#     return [num for num in lst if num % 3 == 0]

# new_lst = [divisible_by_3(el) for el in lst]
# print(new_lst)

# dict1 = {
#     'grape': {
#         'type': 'fruit',
#         'colors': ['red', 'green'],
#         'size': 'small',
#     },
#     'carrot': {
#         'type': 'vegetable',
#         'colors': ['orange'],
#         'size': 'medium',
#     },
#     'apricot': {
#         'type': 'fruit',
#         'colors': ['orange'],
#         'size': 'medium',
#     },
#     'marrow': {
#         'type': 'vegetable',
#         'colors': ['green'],
#         'size': 'large',
#     },
# }

# def select_items(dictionary):
#     if dictionary['type'] == 'fruit':
#         return [el.capitalize() for el in dictionary['colors']]

#     return dictionary['size'].upper()

# new_dict = [select_items(dict1[el]) for el in dict1]
# print(new_dict)

# lst = [
#     {'a': [1, 2, 3]},
#     {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
#     {'e': [8], 'f': [6, 10]},
# ]

# def all_even(list_of_lists):
#     for ls in list_of_lists:
#         if not all([num % 2 == 0 for num in ls]):
#             return False 

#     return True

# filt_lst = [el for el in lst if all_even(el.values())]
# print(filt_lst)

# import random
# letters = list('1234567890abcdef')

# def generate_uuid():
#     uuid = []
#     spans = [8, 4, 4, 4, 12]

#     for s in spans:
#         cur = [random.choice(letters) for _ in range(s)]
#         uuid.append("".join(cur))

#     return "-".join(uuid)

# print(generate_uuid())

# def get_vowels(ls):
#     vowels = []

#     for word in ls:
#         vowels += [letter for letter in word if letter in 'aeiou']

#     return "".join(vowels)

# dict1 = {
#     'first':  ['the', 'quick'],
#     'second': ['brown', 'fox'],
#     'third':  ['jumped'],
#     'fourth': ['over', 'the', 'lazy', 'dog'],
# }

# # Your code goes here

# list_of_vowels = list(''.join([get_vowels(value) for value in dict1.values()]))

# print(list_of_vowels)
# ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']

dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

vowels = [char for key in dict1
                for word in dict1[key]
                for char in word if char in 'aeiou']

print(vowels)