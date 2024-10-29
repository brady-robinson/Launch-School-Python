# Literals are syntactic notation that let's you directly
# represent object in source code

# 'Hello, world!' is a str literal
# {7, 8} is a set literal

# Type constructors are used for objects that don't have
# literal forms

# range(10)
# frozenset([1, 2])

# variable initialization and assignment
pi = 3.14 # initialize the variable pi and assign it to the float
pi = 3.141 # reassign the variable to a different float

# Triple quotes/double/single
print("""The man said, "Hello." And stepped away from the window.""")
print('The man said, "Hello."')

# Raw strings don't recognize escapes
print(r"C:\Users\drive")

# string interpolation
print(f'sum is {1+1}')

# Exercises
# 'True' -> str
# False  -> bool
# (1, 2, 3) -> tuple
# 1.5 -> float
# [1, 2, 3] -> list
# 2 -> int
# range(5) -> range
# {1, 2, 3} -> set
# None -> Nonetype
# {'foo': 'bar'} -> dict