# file = open('example.txt', 'r')
# content = file.read()
# file.close()

# print(repr(content))

# file = open('example.txt', 'r')
# content = file.readlines()
# file.close()

# print(repr(content))

# file = open('example.txt', 'r')
# print(repr(file.readline()))
# print(repr(file.readline()))
# print(repr(file.readline()))
# print(repr(file.readline()))
# file.close()

# file = open('example.txt', 'r')

# for line in file:
#     print(repr(line))

# file.close()

# file = open('output.txt', 'w')
# file.write('Hello, world!\n')

# lines = ['First line\n', 'Second line\n']
# file.writelines(lines)

# file.close()

# file = open('output.txt', 'a')

# file.write('Third line!\n')
# file.write('Last line!\n')
# file.close()

try:
    with open('example1.txt', 'r') as file:
        for line in file:
            print(line)
except FileNotFoundError:
    print('The file does not exist.')