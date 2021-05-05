def interpolation_search(array, k):
    """
    интерполярный поиск по списку
    """
    low, high = 0, len(array) - 1
    while low < high:
        mid = int(low + (high - low) * (k - array[low]) / (array[high] - array[low]))
        if mid < low: mid = low
        if mid > high: mid = high

        if array[mid] == k: return mid
        if k < array[mid]:
            high = mid
        else:
            low = mid
    return -1


def interpolation_search_recursive(array, k, start=0, end=None):
    """
    интерполярный поиск по списку,
    рекурсивный алгоритм
    """
    if end is None:
        end = len(array) - 1

    if start >= end:
        return -1

    mid = int(start + (end - start) * (k - array[start]) / (array[end] - array[start]))
    if mid < start: mid = start
    if mid > end: mid = end

    if k == array[mid]: return mid

    if k < array[mid]:
        return interpolation_search_recursive(array, k, start, mid)
    else:
        return interpolation_search_recursive(array, k, mid, end)
