# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    a = b = 0
    for i in range(elements):
        if a >= len(arrA):
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
        else:
            merged_arr[i] = arrB[b]
            b += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])

    # TO-DO
        arr = merge(left, right)
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO
    start2 = mid + 1
    if arr[mid] <= arr[start2]:
        return

    for i in range(start, end + 1):
        if start > mid:
            arr[i] = start2[right]
            right += 1
        elif right > end:
            arr[i] = start2[left]
            left += 1
        elif start2[right] < start2[left]:
            arr[i] = start2[right]
            right += 1
        else:
            arr[i] = start2[left]
            left += 1
    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    if l <= r:
        return arr
    mid = l + (r - l) // 2
    merge_sort_in_place(arr, l, mid)
    merge_sort_in_place(arr, mid, r)
    arr = merge_in_place(arr, l, mid + 1, r)
    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
