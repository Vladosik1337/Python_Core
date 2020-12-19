def count_letters():
    a = str(input("Enter your text: ")).replace(' ', '')
    i = 0
    print(a)
    for i in range(len(a)):
        i += 1
    print("In this text is", i, "letters")
count_letters()