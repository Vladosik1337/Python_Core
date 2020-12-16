factorial = int(input("Enter your number: "))
o = 1
m = 1
while m <= factorial:
    o = m * o
    m += 1
print(f"Factorial is {o}")