# global scope

# name = 'John'

# def my_func():
#     print(f'Hello, {name}')

# my_func()

# local scope
# function scope

# def my_func():
#     local_var = 10
#     print(local_var)

# my_func()
# print(local_var)

# def my_func():
#     global local_var
#     local_var = 10
#     print(local_var)

# my_func()
# print(local_var)

# block scope

if True:
    block_var = 'Hello'

print(block_var)