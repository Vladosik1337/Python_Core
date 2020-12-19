a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

def longest_number():
    """
    this function longest_number
    return the largest number of
    two numbers
    Output: parameter a, b
    """
    if a > b:
        print(f"{a} > {b}")
    elif a == b:
        print(f"{a} = {b}")
    else:
        print(f"{b} > {a}")

longest_number()

