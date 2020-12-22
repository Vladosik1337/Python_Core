def count_positives_sum_negatives(arr):
    positives_elemetns = 0
    sum_negative_elements = []
    if sum(arr) != 0 or arr != []:
        for value in arr:
            if value > 0:
                positives_elemetns += 1
            else:
                sum_negative_elements.append(value)
    else:
        return []
    list = [positives_elemetns,sum(sum_negative_elements)]
    return list


