def choose_sort(array):
    """простая сортировка выбором"""
    def find_smallest(array):
        smallest = array[0]
        smallest_index = 0
        for i in range(len(array)):
            if array[i] < smallest:
                smallest = array[i]
                smallest_index = i
        return smallest_index
    sorted_arrray = []
    for i in range(len(array)):
        smallest = find_smallest(array)
        sorted_arrray.append(array.pop(smallest))
    return sorted_arrray



