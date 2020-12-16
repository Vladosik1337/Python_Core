num1 = 1
num2 = 1

n = int(input("Enter the number up to which the Fibonacci list will be: "))

if n < 2:
    quit()

print(num1, end=' ')
print(num2, end=' ')
for i in range(2, n):
    num1, num2 = num2, num1 + num2
    print(num2, end=' ')

print()