def binary_Search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1


n = int(input("Enter no. of elements: "))
arr = []

print("Enter Elements:")
for i in range(n):
    arr.append(int(input()))

key = int(input("Enter the element to search: "))

if arr != sorted(arr):
    print("Array is unsorted. Binary search cannot be performed.")
else:
    result = binary_Search(arr, key)

    if result != -1:
        print("Element found at index", result)
    else:
        print("Element not found")
