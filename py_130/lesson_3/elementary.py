def add(a, b):
    return a + b

assert add(3, 4) == 7, "Add function failed"

is_active = True

assert is_active, "Boolean check failed"

def get_max(a, b):
    return max(a, b)

assert get_max(10, 20) > 15, "Comparison check failed"

numbers = [1, 2, 3]
assert 2 in numbers, "Containment check failed"

try:
    x = 1 / 0
    assert False, "xception check failed, no exception raised"
except ZeroDivisionError:
    pass

