# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    for i in range(elements):
        if arrA[i] < arrB[i]:
            elements.append(arrA[merged_arr])
        elif arrB[i] == merged_arr[i]:
            arrA[i] += merged_arr[i]
        elif arrB[i] < arrA[i]:
            merged_arr[i] += arrA[i]
        elif arrA[i] < arrB[i]:
            merged_arr[i] += arrB[i]

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
    print(arr)
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
