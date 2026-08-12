def search(m):
    key=m
    for i in range(n-1):
        if arr[i]==key:
            return i
n=int(input("enter no.of employees to add:"))
arr=[]
for i in range(n):
    a=int(input("enter a value:"))
    arr.append(a)
print(arr)
m=int(input("enter a element to search:"))
result=search(m)
if result==-1:
     print("element is not found")
else:
     print("employee id is stored at the index:",result)
