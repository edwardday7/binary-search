#!/usr/bin/env python3

def binary_search(arr, n):
    low = 0
    mid = 0
    high = len(arr) - 1

    while low <= high:

        mid = (high + low) // 2     # Find midpoint
        if n > arr[mid]:
            low = mid + 1           # Chop off first half of array
        elif n < arr[mid]:
            high = mid - 1          # Chop off second half of array
        else:
            return mid


    return None



def main():

    arr = [1, 3, 5, 14, 29, 49, 68, 94]
    index = binary_search(arr, 94)
    
    if index:
        print("Element found at index: ", index)
    else:
        print("Element not found")


if __name__ == "__main__":
    main()