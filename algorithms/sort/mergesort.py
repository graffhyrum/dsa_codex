# Mergesort

def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_arr = mergesort(arr[:mid])
    right_arr = mergesort(arr[mid:])
    return merge(left_arr, right_arr)


def merge(left_arr, right_arr):
    result = []
    left_idx = 0
    right_idx = 0
    while left_idx < len(left_arr) and right_idx < len(right_arr):
        if left_arr[left_idx] < right_arr[right_idx]:
            result.append(left_arr[left_idx])
            left_idx += 1
        else:
            result.append(right_arr[right_idx])
            right_idx += 1
    if left_idx < len(left_arr):
        result.extend(left_arr[left_idx:])
    if right_idx < len(right_arr):
        result.extend(right_arr[right_idx:])
    return result
