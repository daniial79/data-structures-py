def merge(arr1: list, arr2: list) -> list:
    combined = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            combined.append(arr1[i])
            i += 1
        else:
            combined.append(arr2[j])
            j += 1
    while i < len(arr1):
            combined.append(arr1[i])
            i += 1
    while j < len(arr2):
            combined.append(arr2[j])
            j += 1 
    return combined 

def merge_sort(arr: list) -> list:
    if len(arr) == 1:
        return arr
    mid = int(len(arr) / 2)
    left = arr[:mid]
    right = arr[mid:]
    return merge(merge_sort(left), merge_sort(right))
