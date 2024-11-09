import math

# print(0.3 + 0.6)
# print(math.isclose(0.3 + 0.6, 0.9))

# print(type(float("nan")))
# print(math.isnan(float("nan")))

a = 42
b = 42
c = a

print(id(a) == id(b) == id(c))
print(id(a), id(b), id(c))