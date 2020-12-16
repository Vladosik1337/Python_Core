first_value = input("Input your first number:")
second_value = input("Input your second number:")

print(f"Your first value is {first_value},and second value is {second_value}")

first_value, second_value = second_value, first_value
print(f"After swap,your first value is {first_value},and second value is {second_value}")