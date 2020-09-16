# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    def sort(a_index=0, b_index=0, index=0):
        if index >= len(merged_arr):
            return merged_arr
        else:
            if a_index > len(arrA) - 1:
                merged_arr[index] = arrB[b_index]
                index += 1
                b_index += 1
                sort(a_index, b_index, index)
            elif b_index > len(arrB) - 1:
                merged_arr[index] = arrA[a_index]
                index += 1
                a_index += 1
                sort(a_index, b_index, index)
            elif arrA[a_index] <= arrB[b_index]:
                merged_arr[index] = arrA[a_index]
                index += 1
                a_index += 1
                sort(a_index, b_index, index)
            else:
                merged_arr[index] = arrB[b_index]
                index += 1
                b_index += 1
                sort(a_index, b_index, index)
    sort()
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr
    elif len(arr) > 2:
        #split the array
        split = (len(arr) - 1) // 2
        arrA = arr[0:split]
        arrB = arr[split:len(arr)]
        sortedA = merge_sort(arrA)
        sortedB = merge_sort(arrB)
        return merge(sortedA, sortedB)
    else:
        if arr[0] < arr[1]:
            return arr
        else:
            arr[0], arr[1] = arr[1], arr[0]
            return arr
    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
#def merge_in_place(arr, start, mid, end):
    # Your code here


#def merge_sort_in_place(arr, l, r):
    # Your code here

