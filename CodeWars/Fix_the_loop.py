def list_animals(animals):
    list = ""
    a = 1
    for i in animals:
        list += f"{a}" + '. ' + i + '\n'
        a += 1
    return list


