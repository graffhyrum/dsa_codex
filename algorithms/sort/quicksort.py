# Quicksort

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        # Sub-array of all the elements less than the pivot
        less = [i for i in array[1:] if i <= pivot]
        # Sub-array of all the elements greater than the pivot
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)