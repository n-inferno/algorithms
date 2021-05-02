def bubble_sort(arr):
    """функция пузырьковой сортировки по возрастанию"""
    flag = True
    while flag:
        flag = False
        for i in range(1, len(arr)):
            if arr[i] < arr[i-1]:
                flag = True
                arr[i], arr[i-1] = arr[i-1], arr[i]
    return arr


