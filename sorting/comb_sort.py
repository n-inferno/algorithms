def comb_sort(arr):
    diff = len(arr) - 1
    flag = True
    while diff > 1 or (flag and diff == 1):
        flag = False
        i = 0
        while i + diff < len(arr):
            if arr[i] > arr[i + diff]:
                arr[i], arr[diff + i] = arr[diff + i], arr[i]
                flag = True
            i += 1

        if diff != 1:
            diff = int(diff // 1.247)
    return arr
