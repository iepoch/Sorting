# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        for j in range(smallest_index+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # (hint, can do in 3 loc)

        # TO-DO: swap
        if smallest_index != cur_index:
            arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
    print(f'This is the Select Sort {arr}\n')
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Get the first index of the array
    for i in range(0, len(arr) - 1):
        # Find the smallest index
        for j in range(0, len(arr) - 1 - i):
            # If the index is greater than the index before it then swap them
            if arr[j] > arr[j + 1]:
                # Here we want to start swaping the values
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(f'This is the Bubble Sort {arr}\n')
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
