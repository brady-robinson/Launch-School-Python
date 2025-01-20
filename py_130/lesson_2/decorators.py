# def my_decorator(func):
#     def wrapper():
#         print("Before the fnction call")
#         func()
#         print("After the function call")

#     return wrapper

# def say_hello():
#     print("Hello!")

# def my_decorator(func):
#     def wrapper():
#         print("Before the fnction call")
#         func()
#         print("After the function call")

#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello!")

# # decorated_hello = my_decorator(say_hello)
# # decorated_hello()

# say_hello()

# from time import perf_counter
# from functools import lru_cache

# @lru_cache
# def is_prime(n):
#     for i in range(2, n):
#         if (n % i) == 0:
#             return False
        
#     return True

# start_time = perf_counter()
# is_prime(73729261)
# end_time = perf_counter()
# print(f"{end_time - start_time} seconds.")

# start_time = perf_counter()
# is_prime(73729261)
# end_time = perf_counter()
# print(f"{end_time - start_time} seconds.")

# start_time = perf_counter()
# is_prime(73729261)
# end_time = perf_counter()
# print(f"{end_time - start_time} seconds.")

from time import perf_counter
from functools import lru_cache

def time_runs(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        return_value = func(*args, **kwargs)
        print(f"The function ran in {perf_counter()-start} seconds")
        return return_value
    
    return wrapper

@time_runs
@lru_cache
def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False

    return True

is_prime(73729261)
is_prime(73729261)