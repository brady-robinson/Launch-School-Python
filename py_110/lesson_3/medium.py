# import copy

# def rotate_list(ls):
#     if type(ls) is not list:
#         return
#     if len(ls) == 0:
#         return ls
    
#     ls_deep_copy = copy.deepcopy(ls)
#     ls_deep_copy.append(ls_deep_copy[0])
#     ls_deep_copy.pop(0)

#     return ls_deep_copy


# # All of these examples should print True

# print(rotate_list([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7])
# print(rotate_list(['a', 'b', 'c']) == ['b', 'c', 'a'])
# print(rotate_list(['a']) == ['a'])
# print(rotate_list([1, 'a', 3, 'c']) == ['a', 3, 'c', 1])
# print(rotate_list([{'a': 2}, [1, 2], 3]) == [[1, 2], 3, {'a': 2}])
# print(rotate_list([]) == [])

# # return `None` if the argument is not a list
# print(rotate_list(None) == None)
# print(rotate_list(1) == None)

# # the input list is not mutated
# lst = [1, 2, 3, 4]
# print(rotate_list(lst) == [2, 3, 4, 1])
# print(lst == [1, 2, 3, 4])

# def rotate_rightmost_digits(num, digits):
#     count = digits
#     rightmost_reverse = 0
#     mult = 1

#     while count > 0 and num > 0:
#         rightmost_reverse *= 10
#         rightmost_reverse += num % 10
#         num //= 10
#         count -= 1
#         mult *= 10

#     right_most_single = rightmost_reverse % 10
#     rightmost_reverse = rightmost_reverse // 10
#     second_reverse = 0

#     while rightmost_reverse > 0:
#         second_reverse *= 10
#         second_reverse += rightmost_reverse % 10
#         rightmost_reverse //= 10

#     second_reverse *= 10
#     second_reverse += right_most_single
    
#     num = num * mult
#     num += second_reverse
    
#     return num


# print(rotate_rightmost_digits(735291, 2) == 735219)  # True
# print(rotate_rightmost_digits(735291, 3) == 735912)  # True
# print(rotate_rightmost_digits(735291, 1) == 735291)  # True
# print(rotate_rightmost_digits(735291, 4) == 732915)  # True
# print(rotate_rightmost_digits(735291, 5) == 752913)  # True
# print(rotate_rightmost_digits(735291, 6) == 352917)  # True
# print(rotate_rightmost_digits(1200, 3) == 1002)      # True

# Data structures
# - none only string and int

# algo
# write a reverse function that takes a string and reverses it
# maintain a counter that tracks where in the input you are
# slice the input into two halves corresponding to the counter
# reverse the right half
# concat the two halves
# continue until the counter equals the length of the input

# def reverse(string):
#     if len(string) == 0:
#         return string
    
#     string += string[0]
#     return string[1:]

# def max_rotation(num):
#     str_num = str(num)
#     count = 0

#     while count <= len(str_num):
#         left = str_num[:count]
#         right = str_num[count:]
#         right = reverse(right)
#         str_num = left + right
#         count += 1

#     return int(str_num)

# print(max_rotation(735291) == 321579)          # True
# print(max_rotation(3) == 3)                    # True
# print(max_rotation(35) == 53)                  # True
# print(max_rotation(8703529146) == 7321609845)  # True

# # Note that the final sequence here is `015`. The leading
# # zero gets dropped, though, since we're working with
# # an integer.
# print(max_rotation(105) == 15)                 # True

# def word_to_digit(message):
#     digits = {'zero':'0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
#               'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
#     message = message.split()

#     for i in range(len(message)):
#         if message[i] in digits:
#             message[i] = digits[message[i]]

#     return " ".join(message)

# message = 'Please call me at five five five one two three four'
# print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# # Should print True

#pedac

# data structures
# input: int
# output: bool

# algo
# starting from 2
# increment the val by 1
# on each iteration until we reach the input val
# check if the val evenly divides the input
# if so, return true
# return false if by the end there are no return true vals

# def is_prime(num):
#     if num <= 1:
#         return False
    
#     count = 2

#     while count < num:
#         if num % count == 0:
#             return False
#         count += 1

#     return True

# print(is_prime(1) == False)              # True
# print(is_prime(2) == True)               # True
# print(is_prime(3) == True)               # True
# print(is_prime(4) == False)              # True
# print(is_prime(5) == True)               # True
# print(is_prime(6) == False)              # True
# print(is_prime(7) == True)               # True
# print(is_prime(8) == False)              # True
# print(is_prime(9) == False)              # True
# print(is_prime(10) == False)             # True
# print(is_prime(23) == True)              # True
# print(is_prime(24) == False)             # True
# print(is_prime(997) == True)             # True
# print(is_prime(998) == False)            # True
# print(is_prime(3_297_061) == True)       # True
# print(is_prime(23_297_061) == False)     # True

# def fibonacci(num):
#     if num == 1 or num == 2:
#         return 1
    
#     num_1 = 1
#     num_2 = 1

#     for i in range(2,num):
#         fib = num_1 + num_2
#         num_1 = num_2
#         num_2 = fib

#     return fib

# data structure
# dictionary

# algo
# on each iteration, check if we have seen the num - 1 and num -2 before
# if we have seen them before, save their sum 
cache = {1:1, 2:1}

def fibonacci(num):
    if num <= 2:
        return 1
    elif num in cache:
        return cache[num]
    else:
        cache[num] = fibonacci(num - 1) + fibonacci(num - 2)
        return cache[num]

print(fibonacci(1) == 1)         # True
print(fibonacci(2) == 1)         # True
print(fibonacci(3) == 2)         # True
print(fibonacci(4) == 3)         # True
print(fibonacci(5) == 5)         # True
print(fibonacci(6) == 8)         # True
print(fibonacci(12) == 144)      # True
print(fibonacci(20) == 6765)     # True