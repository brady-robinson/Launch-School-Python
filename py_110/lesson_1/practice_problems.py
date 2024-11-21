# fruits = ("apple", "banana", "cherry", "date", "banana")
# print(fruits.count('banana'))

# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# c = a.union(b)
# print(c)

# ages = {
#     "Herman": 32,
#     "Lily": 30,
#     "Grandpa": 5843,
#     "Eddie": 10,
#     "Marilyn": 22,
#     "Spot": 237,
# }

# print(sum(ages.values()))
# print(min(ages.values()))

statement = "The Flintstones Rock"
counts = {}

for letter in statement:
    counts[letter] = counts.get(letter, 0) + 1

print(counts)