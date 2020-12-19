list_of_numbers_divisible_2 = []
list_of_numbers_divisible_3 = []
list_of_numbers_not_divisible_2_and_3 = []

for i in range(1,11):
    if i % 2 == 0:
        list_of_numbers_divisible_2.append(i)
    elif i % 3 == 0:
        list_of_numbers_divisible_3.append(i)
    else:
        list_of_numbers_not_divisible_2_and_3.append(i)

print(f"List of numbers divisible 2 is {list_of_numbers_divisible_2}\nList of numbers divisible 3 is {list_of_numbers_divisible_3}\nList of numbers that not divisible 2 and 3 is {list_of_numbers_not_divisible_2_and_3}")