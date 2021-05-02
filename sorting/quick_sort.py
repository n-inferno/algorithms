def quick_sort(array):
    """
    функция быстрой сортировки по возрастанию
    """
    if len(array) < 2:
        return array
    pivot = array[0]
    less = []
    greater = []
    mid = []
    for i in range(len(array)):
        if array[i] < pivot:
            less.append(array[i])
        elif array[i] > pivot:
            greater.append(array[i])
        else:
            mid.append(array[i])
    return quick_sort(less) + mid + quick_sort(greater)

