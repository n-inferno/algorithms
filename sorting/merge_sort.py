def merge_sort(arr):
    """
    сортировка слиянием
    """
    def merge(arr1, arr2):
        merged = []
        while arr1 or arr2:
            if not arr2:
                merged.append(arr1.pop(0))
            elif not arr1:
                merged.append(arr2.pop(0))
            else:
                merged.append(arr1.pop(0)) if arr1[0] <= arr2[0] else merged.append((arr2.pop(0)))
        return merged

    if len(arr) <= 1:
        return arr

    left = arr[:len(arr) // 2]
    right = arr[len(arr) // 2:]
    return merge(merge_sort(left), merge_sort(right))
