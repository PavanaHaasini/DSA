def Insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1

        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr

n=int(input("Enter no. of Elements:"))
arr=[]
print("Enter Elements:")

for i in range(n):
    arr.append(int(input()))

Insertion_sort(arr)
print("Sorted array:")
for element in arr:
    print(element, end=" ")
