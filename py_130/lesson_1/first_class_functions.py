# def hello():
#     print("hello")

# hi = hello
# hello()
# hi()

# def square(num):
#     return num**2

# nums = [1, 2, 3, 4]

# transformed_nums = map(square, nums)
# print(list(transformed_nums))

# square = lambda number: number**2
# hello = lambda: print('hello')
# add3 = lambda num1, num2, num3: num1 + num2 + num3

# print(square(2))

result = map(lambda x: x**2, [1, 2, 3])
print(list(result))