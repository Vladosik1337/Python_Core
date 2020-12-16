#1
numbers = 7932
product_of_numbers = 1

while (numbers != 0):
    product_of_numbers = product_of_numbers * (numbers % 10)
    numbers = numbers // 10

print(f"Product_of_numbers = {product_of_numbers}")

#2
numbers = 7932
reverse_numbers = str(numbers)[::-1]
print(f"Reverse_numbers = {reverse_numbers}")

#3
numbers = 7932
sort_numbers = sorted(str(numbers))
str_sort_numbers = "".join(sort_numbers)
int_sort_numbers = int(str_sort_numbers)
print(f"Sort_numbers = {int_sort_numbers}")