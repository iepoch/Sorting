# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

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
       # TO-DO
    # First need to divide
    if len(arr) > 1:
        midpoint = int(len(arr) / 2)
        # Recursive call where it calls itself
        left = merge_sort(arr[:midpoint])
        right = merge_sort(arr[midpoint:])
        # will merge back latter
        arr = merge(left, right)
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    pass
    # left = arr[start:mid]
    # right = arr[mid:end]
    # a = 0
    # b = 0

    # for i in range(start, end):
    #     if b >= len(right) or (a < len(left) and left[a] < right[b]):
    #         arr[i] = left[a]
    #         a += 1
    #     else:
    #         arr[i] = right[b]
    #         b += 1
    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO
    l = 0
    r = len(arr - 1)
    if (r - l) > len:
        mid = int((l+r) / 2)
        merge_sort_in_place(arr, l, mid)
        merge_sort_in_place(arr, mid, r)
    arr = merge_in_place(arr, l, mid, r)
    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
