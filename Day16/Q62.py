n=int(input("enter the number of elements"))
arr=[]
print("enter the elements")
for i in range(n):
    element=int(input())
    arr.append(element)

max_count=0
element=arr[0]

for i in range(len(arr)):
    current_count=0
    for j in range(len(arr)):
        if arr[i]==arr[j]:
            current_count+=1

    if current_count>max_count:
     max_count=current_count
     element=arr[i]
print(element)