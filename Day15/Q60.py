n=int(input("enter the number of elements:"))
arr=[]
print("enter the elements:")
for i in range(n):
    element=int(input())
    arr.append(element)

l=len(arr)
position=0
for i in range(l):
    if arr[i]!=0:
        temp=arr[i]
        arr[i]=arr[position]
        arr[position]=temp
        position+=1
print(arr)
    