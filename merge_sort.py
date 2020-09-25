def merge(arr1, arr2):
    """
    объединение двух отсортированных массивов
    """
    merged_arr = []
    while arr1 and arr2:
        if not arr2 or arr1[0] <= arr2[0]:
            merged_arr.append(arr1[0])
            arr1 = arr1[1:]
        else:
            merged_arr.append(arr2[0])
            arr2 = arr2[1:]
    if arr1:
        merged_arr.extend(arr1)
    if arr2:
        merged_arr.extend(arr2)
    return merged_arr


def merge_sort(arr):
    """
    сортировка слиянием
    """
    if len(arr) == 1:
        return arr
    else:
        m = len(arr) // 2
        return merge(merge_sort(arr[:m]), merge_sort(arr[m:]))
