# nums = [1, 2]
# tup = (3, 4)

# combo_ls = [*nums, *tup]
# combo_tup = (*nums, *tup)
# combo_set = {*nums, *tup}

# print(combo_ls)
# print(combo_tup)
# print(combo_set)

# def add(num1, num2, num3):
#     return num1 + num2 + num3

# nums = [1, 2, 3]
# print(add(*nums))

dict1 = {'a': 1, 'b': 2}

def profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

profile(**dict1)