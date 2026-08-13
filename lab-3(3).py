def Selection_sort(arr):
    n=len(arr)
    for i in range(n-1):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index] = arr[min_index],arr[i]
    return arr

n=int(input("Enter no. of Elements:"))
arr =[]
print("Enter Elements:")
for i in range (n):
    arr.append(int(input()))
Selection_sort(arr)

print("Sorted array:", arr)
for element in arr:
    print(element,end=" ")
