n=int(input("enter the number of elements:"))
array=[]
print("enter the elements:")
for i in range(n):
    element=int(input())
    array.append(element)

target=int(input("enter the target element:"))

count=0
for num in array:
        if num==target:
            count+=1

print("frequency:",count) 