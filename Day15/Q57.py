n=int(input("enter the number of elements:"))
arr=[]
print("enter the elements:")
for i in range(n):
    elements=int(input())
    arr.append(elements)


l=len(arr)
for i in range(l//2):
        temp=arr[i]
        arr[i]=arr[l-1-i]
        arr[l-1-i]=temp
       
print("reversed array:",arr)
