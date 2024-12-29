# number = None

# while True:
#     number = input('Enter number: ')

#     try:
#         number = float(number)
#         break
#     except ValueError:
#         print('Oops!')

# print(f'Thanks! You entered {number}')

# def foo1():

#     # raise ZeroDivisionError('Got ZeroDivisionError')
#     # raise ValueError('Got ValueError')
#     raise AttributeError('Got AttributeError')
#     print('We should not be here')

# def foo2():
#     try:
#         foo1()
#     except ZeroDivisionError:
#         print('Got ZeroDivisionError')

# def foo3():
#     try:
#         foo2()
#     except ValueError:
#         print('Got ValueError')

# foo3()

# for value in ['abc', '0']:
#     try:
#         num = float(value)
#         quotient = 10 / num
#         break
#     except ValueError as e:
#         print(f'Error!\n{e}\n')
#     except ZeroDivisionError as e:
#         print(f'Error!\n{e}\n')
#     finally:
#         print('Done.')

# num1 = int(input('first num: '))
# num2 = int(input('second num: '))

# try:
#     num3 = num1 / num2
# except (ZeroDivisionError, ValueError) as e:
#     print(f"Error: {e}")
# else:
#     print(f'Result: {num3}')
# finally:
#     print("End of program.")

# class NegativeNumberError(ValueError):
#     pass

# num1 = float(input('First num: '))

# if num1 < 0:
#     raise NegativeNumberError("Num must be positives or zero")

# print(f'Num: {num1}')

# def inverse(nums):
#     output = []

#     for n in nums:
#         try:
#             n = float(n)
#             output.append(1 / n)
#         except ZeroDivisionError or ValueError:
#             output.append(0)

# students = {'John': 25, 'Jane': 22, 'Doe': 30}

# def get_age(name):
#     try:
#         return students[name]
#     except KeyError:
#         return 'Student not found.'

numbers = [1, 2, 3, 4, 5]

def lbyl(nums):
    if len(nums) < 6:
        return None
    
    return nums[5]

def afnp(nums):
    try:
        return nums[5]
    except IndexError:
        return None