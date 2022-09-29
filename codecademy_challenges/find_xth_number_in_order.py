score_list = [1, 2, 3, 9999, 13]
top = 10000


def score_sorter(array, top_score):
    temp = 0

    for a in range(0, len(array)):
        for b in range(a+1, len(array)):
            if array[a] < array[b]:
                temp = array[a]
                array[a] = array[b]
                array[b] = temp
    return array, top_score



print(score_sorter(score_list, top))



