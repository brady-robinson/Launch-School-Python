import pdb

# def is_real_palindrome(chars):
#     chars = list(chars)
#     chars = [c.lower() for c in chars if c.isalnum()]
#     rev_chars = list(reversed(chars))

#     # pdb.set_trace()

#     return chars == rev_chars

# print(is_real_palindrome('madam') == True)           # True
# print(is_real_palindrome('356653') == True)          # True
# print(is_real_palindrome('356635') == False)         # True
# print(is_real_palindrome('356a653') == True)         # True
# print(is_real_palindrome('123ab321') == False)       # True

# # case doesn't matter
# print(is_real_palindrome('Madam') == True)           # True

# # only alphanumerics matter
# print(is_real_palindrome("Madam, I'm Adam") == True) # True

# def running_total(num_list):
#     output = []
#     total = 0

#     for num in num_list:
#         total += num
#         output.append(total)

#     return output

# print(running_total([2, 5, 13]) == [2, 7, 20])    # True
# print(running_total([14, 11, 7, 15, 20])
#       == [14, 25, 32, 47, 67])                    # True
# print(running_total([3]) == [3])                  # True
# print(running_total([]) == [])                    # True

# def word_sizes(words):
#     output = {}
#     words = list(words)
#     words = [c for c in words if c.isalpha() or c.isspace()]
#     words = "".join(words)
#     words = words.split()

#     for word in words:
#         output[len(word)] = output.get(len(word), 0) + 1

#     return output

# string = 'Four score and seven.'
# print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

# string = 'Hey diddle diddle, the cat and the fiddle!'
# print(word_sizes(string) == {3: 5, 6: 3})

# string = 'Humpty Dumpty sat on a w@ll'
# print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

# string = "What's up doc?"
# print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

# print(word_sizes('') == {})

# def swap_word(word):
#     word = list(word)
#     word[0], word[-1] = word[-1], word[0]

#     return "".join(word)

# def swap(words):
#     words = words.split()

#     for i in range(len(words)):
#         words[i] = swap_word(words[i])

#     return " ".join(words)

# print(swap('Oh what a wonderful day it is')
#       == "hO thaw a londerfuw yad ti si")  # True
# print(swap('Abcde') == "ebcdA")            # True
# print(swap('a') == "a")                    # True

# def string_to_signed_integer(string):
#     output = 0
#     sign = 1

#     for num in string:
#         if num in "+-":
#             sign = -1 if num == '-' else 1
#         else:
#             num = ord(num) - ord('0')
#             output *= 10
#             output += num

#     return sign * output

# # print(string_to_integer("4321") == 4321)  # True
# # print(string_to_integer("570") == 570)    # True

# print(string_to_signed_integer("4321") == 4321)  # True
# print(string_to_signed_integer("-570") == -570)  # True
# print(string_to_signed_integer("+100") == 100)   # True

# def signed_integer_to_string(integer):
#     digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
#     sign = "+" if integer > 0 else "-"
#     integer = integer * -1 if integer < 0 else integer
#     output = ""

#     while integer > 0:
#         num = integer % 10
#         integer = integer // 10
#         output = digits[num] + output

#     return sign + output if output else '0'

# print(signed_integer_to_string(4321) == "+4321")  # True
# print(signed_integer_to_string(-123) == "-123")   # True
# print(signed_integer_to_string(0) == "0")         # True