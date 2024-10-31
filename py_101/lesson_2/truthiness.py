# print(True)
# print(False)

# def make_longer(string, longer):
#     if longer:
#         return string + string 
#     else:
#         return string

# print(make_longer("abc", True))
# print(make_longer("xyz", False))

# def is_digit(char):
#     if '0' <= char <= '9':
#         return True
#     else:
#         return False

# print(is_digit('5'))
# print(is_digit('a'))

# value = True
# if value is True:
#     print("It's True")
# elif value is False:
#     print("It's false!")
# else:
#     print("It's not true of false!")

# num = 5
# if num < 10:
#     print("small number")
# else:
#     print("large number")

# def is_small(number):
#     return number < 10

# num = 15

# if is_small(num):
#     print("small number")
# else:
#     print("large number")

# print(True and True)
# print(True and False)
# print(False and True)
# print(False and False)

# num = 5
# print((num < 10) and (num > 3))
# print((num < 10) and (num > 6))
# print((num > 10) and (num < 6))
# print((num > 10) and (num < 3))

# num = 5

# print((num < 10) and (num > 0) and ((num % 2) == 1))
# print((num < 10) and (num > 0) and ((num % 2) == 1) and False)


# print(True or True)
# print(True or False)
# print(False or True)
# print(False or False)

# num = 5
# print((num < 10) or (num > 3))
# print((num < 10) or (num > 6))
# print((num > 10) or (num < 6))
# print((num > 10) or (num < 3))

# print(not True)
# print(not False)

# value = 3
# is_even = (value % 2 == 0)
# print(is_even)
# print(not is_even)

# short circuiting - python stops evaluaitng
# sub expressions when a subexpression once
# it can determine the final value

# print(False and len('1' + 1)) # doesn't generate error
# print(True or len('1' + 1)) # doesn't generate error

# name = 'BOB'
# if name != None and name.isupper():
#     print(f"Hi, {name}")
# else:
#     print("UPPERCASE YOUR NAME")

# falsey values in python
# False
# 0
# 0.0
# None
# 0j
# ""
# []
# {}
# ()
# set()
# frozenset()
# range(0)

num = 5
if num:
    print("valid number")
else:
    print("error")

print(num == True)