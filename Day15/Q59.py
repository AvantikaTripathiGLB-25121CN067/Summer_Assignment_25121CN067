n=int(input("enter the number of elements:"))
arr=[]
print("enter the elements:")
for i in range(n):
    elements=int(input())
    arr.append(elements)

l=len(arr)
if n>1:
    last_element=arr[n-1]
    for i in range(n-1,0,-1):
        arr[i]=arr[i-1]
    arr[0]=last_element

print("right rotated array:",arr)
