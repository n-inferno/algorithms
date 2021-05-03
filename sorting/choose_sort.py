def choose_sort(array):
    """простая сортировка выбором"""
    i = 0
    while i < len(array):
        index_min = i
        min_num = array[i]
        j = i
        while j < len(array):
            if array[j] < min_num:
                min_num = array[j]
                index_min = j
            j += 1
        array[i], array[index_min] = array[index_min], array[i]
        i += 1
    return array
