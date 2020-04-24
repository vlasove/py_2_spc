def binary_search(arr, item):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = int((low + high) / 2)
        sample = arr[mid]

        if sample == item:
            return mid 
        elif sample > item:
            high = mid - 1
        else:
            low = mid + 1
    return None 

array = [1,2,3,4,5,6,7,8,9]
print(binary_search(array, 6))

5 in array 
