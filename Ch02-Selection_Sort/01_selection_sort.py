def find_smallest_index(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest_index = i
            smallest = arr[i]
        
    return smallest_index

def selection_sort(arr):
    new_arr = []

    for i in range(len(arr)):
        smallest = find_smallest_index(arr)
        new_arr.append(arr.pop(smallest))

    return new_arr

print([5, 3, 6, 2, 10])
print(selection_sort([5, 3, 6, 2, 10]))