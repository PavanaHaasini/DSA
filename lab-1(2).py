def interest(p,n):
    if n==0:
        return 1
    else:
        return p*interest(p,n-1)
n=int(input("Enter no.of years:"))
p=int(input("Enter a number:"))
res=inteerest(p,n)
print(res)
