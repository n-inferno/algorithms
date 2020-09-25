def shaker_sort(arr):
    """шейкерная сортировка по возрастанию"""
    left = 1
    right = len(arr)
    while left <= right:
        for i in range(left, right):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
        right -= 1
        for i in range(right - 1, left - 1, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
        left += 1
    return arr
