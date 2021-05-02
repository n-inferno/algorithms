def insert_sort(arr):
    '''
    сортировка вставками
    '''
    for i in range(1, len(arr)):
        j = i
        while j >= 1 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr

