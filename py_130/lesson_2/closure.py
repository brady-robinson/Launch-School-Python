# def create_greeting():
#     greeting = 'hello'
#     print(hex(id(greeting)))

#     def display_greeting():
#         print(greeting)

#     return display_greeting

# greet = create_greeting()
# print(greet.__closure__)

# def add(x, y):
#     return x + y

# def make_adder(x):
#     def adder(y):
#         return add(x, y)
    
#     return adder

# add100 = make_adder(100)
# print(add100(10))

# from functools import partial

# def add(x, y):
#     return x + y

# add1 = partial(add, 1)
# print(add1(5))

# adders = []
# for n in range(1, 4):
#     adders.append(lambda x, n=n: n + x)

# add1, add2, add3 = adders
# print(add1(10))
# print(add2(10))
# print(add3(10))

# adders = []

# for n in range(1, 4):
#     def create_adder(x, n=n):
#         return x + n
    
#     adders.append(create_adder)

# def later(func, argument):

#     def inner():
#         return func(argument)

#     return inner

# def printer(message):
#     print(message)

# print_warning = later(printer, "The system is shutting down!")
# print_warning()  # The system is shutting down!

def later2(func, first_arg):

    def inner(second_arg):
        return func(first_arg, second_arg)

    return inner

def notify(message, when):
    print(f"{message} in {when} minutes!")

shutdown_warning = later2(notify, "The system is shutting down")
shutdown_warning(30) # The system is shutting down in 30 minutes!