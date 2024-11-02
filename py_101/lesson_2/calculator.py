def prompt(message):
    return f"=> {message}"

def invalid_num(num):
    try:
        int(num)
    except ValueError:
        return True

    return False

print("Welcome!")

# Ask user for first number
first_num = input(prompt("What's the first number?\n"))

while invalid_num(first_num):
    print("Invalid number")
    first_num = input(prompt("What's the first number?\n"))

# Ask user for second number
second_num = input(prompt("What's the second number?\n"))

while invalid_num(second_num):
    print("Invalid number")
    second_num = input(prompt("What's the second number?\n"))

print(f'{first_num} {second_num}')
# Ask user for an operation type
operation_type = input(prompt("""What type of operation?
1) Add 2) Subtract 3) Multiply 4) Divide\n"""))

while operation_type not in "1234":
    print("Invalid operation")
    operation_type = input(prompt("""What type of operation?
    1) Add 2) Subtract 3) Multiply 4) Divide\n"""))

first_num = int(first_num)
second_num = int(second_num)
# Perform operation
match operation_type:
    case '1':
        output = first_num + second_num
    case '2':
        output = first_num - second_num
    case '3':
        output = first_num * second_num
    case '4':
        output = first_num / second_num

# Print the result
print(prompt(f"The result is: {output}"))