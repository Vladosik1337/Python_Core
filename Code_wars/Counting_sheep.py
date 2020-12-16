def count_sheeps(sheep):
    count = 0
    for i in sheep:
        if i == True:
            count += 1
        else:
            continue
    return count