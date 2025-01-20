# def greet_all(*names):
#     for name in names:
#         print(f'Hello, {name}.')

# greet_all('Chris', 'Pete', 'Nick')

# greet_all(*['Chris', 'Pete', 'Nick'])

# names = ['Chris', 'Pete', 'Nick']
# chris, pete, nick = names
# print(chris, pete, nick)

nums = [10, 50, 20, 30, 40, 60, 70]
*nums1, nums2 = nums

print(nums1)
print(nums2)