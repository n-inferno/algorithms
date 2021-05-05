def binary_search(array, k):
    """бинарный поиск элемента в упорядоченном списке"""
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if array[mid] == k:
            return mid + 1
        elif array[mid] > k:
            high = mid - 1
        elif array[mid] < k:
            low = mid + 1
    return -1


def binary_search_recursive(array, k, start=0, end=None):
    """
    бинарный поиск элемента в упорядоченном списке,
    рекурсивный алгоритм
    """
    if end is None:
        end = len(array) - 1
    mid = start + (end - start) // 2
    if array[mid] == k:
        return mid
    if start == end:
        return -1
    if k < array[mid]:
        return binary_search_recursive(array, k, start, mid)
    else:
        return binary_search_recursive(array, k, mid + 1, end)
