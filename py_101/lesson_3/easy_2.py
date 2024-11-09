# numbers = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]
# print(numbers[::-1])
# print(list(reversed(numbers)))

# numbers = [1, 2, 3, 4, 5, 15, 16, 17, 95, 96, 99]

# number1 = 8  # False (not in numbers)
# number2 = 95 # True (in numbers)

# print(number1 in numbers)
# print(number2 in numbers)

# print(10 <= 42 <= 100)
# print(100 <= 42 <= 101)
# print(42 in range(10, 101))

# nums = [1, 2, 3, 4, 5]
# # nums.pop(2)
# # print(nums)
# del nums[2]
# print(nums)

# numbers = [1, 2, 3, 4]
# table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}

# print(type(numbers)==list)
# print(isinstance(numbers, list))
# print(type(numbers) is list)
# print(type(table)==list)

# title = "Flintstone Family Members"
# print(title.center(40))

# statement1 = "The Flintstones Rock!"
# statement2 = "Easy come, easy go."
# print(statement1.count("t"))
# print(statement2.count("t"))

# ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 402, 'Eddie': 10}
# print('Spot' in ages)

ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 5843, 'Eddie': 10}
additional_ages = {'Marilyn': 22, 'Spot': 237}
ages.update(additional_ages)
print(ages)