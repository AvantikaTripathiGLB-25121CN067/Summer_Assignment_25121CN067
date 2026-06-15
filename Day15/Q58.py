n=int(input("enter the number of elements:"))
arr=[]
print("enter the elements:")
for i in range(n):
    elements=int(input())
    arr.append(elements)

l=len(arr)
if n>1:
    first_element=arr[0]
    for i in range(n-1):
        arr[i]=arr[i+1]
    arr[n-1]=first_element

print("left rotated array:",arr)

