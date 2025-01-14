# (number for number in range(1_000_000))

# squares = (number**2 for number in [1, 3, 7, 11])

# for square in squares:
#     print(square)
#     print('first loop')
#     if square > 1:
#         break

# for square in squares:
#     print('not first loop')
#     print(square)

# def count_up_to(max_count):
#     count = 1
#     while count <= max_count:
#         yield count
#         count += 1

# counter = count_up_to(5)
# for number in counter:
#     print(number)

# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))

# gen = (1/num for num in range(1,11))

# for num in gen:
#     print(num)

# def reciprocal_gen(n):

#     for num in range(1, n+1):
#         yield 1 / num

# nums = reciprocal_gen(10)

# for num in nums:
#     print(num)

strings = ['hello', 'goodbye']
# cap_string = (word.capitalize() for word in strings)
# print(tuple(cap_string))

def capitalizer(strings):

    for s in strings:
        yield s.capitalize()

cap_strings = capitalizer(strings)
print(tuple(cap_strings))