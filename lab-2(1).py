def linear_Search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

n=int(input("Enter no. of elements:"))
arr=[]
print("Enter Elements:")

for i in range(n):
    arr.append(int(input()))
key = int(input("Enter the elements to search:"))
result= linear_Search (arr,key)

if result!=-1:
    print("Enter found at index",result)
else:
    print("Element not found")
