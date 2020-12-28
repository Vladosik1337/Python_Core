day = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}

try:
    inp_number = int(input("Enter number: "))
    if inp_number <= 0:
        raise ValueError("Please enter positive number!!!")
    if inp_number >= 8:
        raise ValueError("Please enter number less 8")
    else:
        print(day[inp_number])
except TypeError as e:
    print("Please enter number(int) not letter(str)", e)

except ValueError as e:
    print(e)

else:
    print("Nothing went wrong")



