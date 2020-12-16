def enough(cap, on, wait):
    if on + wait <= cap:
        return 0
    else:
        return wait + on - cap


print(enough(10, 5, 5))
print(enough(100, 60, 50))
print(enough(20, 5, 5))
