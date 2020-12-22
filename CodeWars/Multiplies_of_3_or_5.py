def solution(number):
    sum_number = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            sum_number += i
        elif i <= 0:
            return 0
    return sum_number
