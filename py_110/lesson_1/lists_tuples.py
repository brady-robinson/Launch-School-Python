# nums = ['1', '13', '2', '2', '3']
# print(nums.index(3, 3))
# print(nums.count(3))
# nums.insert(1, 5)
# nums.extend([8,9,10])
# nums.remove(1)
# nums.pop(1)
# nums.sort(key=int)
# print(nums)

# tup = (1, 2, 3)
# one, two, three = tup
# print(one)
# print(two)
# print(three)
# print(tup.count(1))
# print(tup.index(2))
# print(tup.index(0))

tup = (5, 6, 7)

for idx, item in enumerate(tup):
    print(f"{idx}: {item}")