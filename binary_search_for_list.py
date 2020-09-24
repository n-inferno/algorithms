def binary_search(array, k):
    """бинарный поиск элемента в упорядоченном списке"""
    low = 0
    high = len(array)-1
    while low <= high:
        mid = low + (high-low)//2
        if array[mid] == k:
            return mid + 1
        elif array[mid] > k:
            high = mid - 1
        elif array[mid] < k:
            low = mid + 1
    return -1

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    keys = list(map(int, input().split()))
    for key in keys:
        print(binary_search(arr, key), end=' ')