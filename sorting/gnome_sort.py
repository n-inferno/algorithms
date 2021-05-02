def gnome_sort(arr):
    """Гномья сортировака по возрастанию"""
    pointer = 1
    i = 1
    while i < len(arr):
        while arr[i] < arr[i - 1] and i != 0:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1
        pointer += 1
        i = pointer

    return arr
