print("Welcome!")

# Ask user for first number
first_num = int(input("What's the first number? "))

# Ask user for second number
second_num = int(input("What's the second number? "))

print(f'{first_num} {second_num}')
# Ask user for an operation type
operation_type = input("What type of operation?\n1) Add 2) Subtract 3) Multiply 4) Divide\n")

# Perform operation
if operation_type == '1':
    output = first_num + second_num
elif operation_type == '2':
    output = first_num - second_num
elif operation_type == '3':
    output = first_num * second_num
elif operation_type == '4':
    output = first_num / second_num

# Print the result
print(f"The result is: {output}")