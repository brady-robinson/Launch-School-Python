import pdb

def add_n(n, num):
    counter = 0

    while counter < n:
        pdb.set_trace()
        num += 1
        counter += 1

    return num

add_n(10, 5)