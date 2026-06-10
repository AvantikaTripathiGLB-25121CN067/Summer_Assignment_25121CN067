n=int(input("enter the number of elements:"))
array=[]
print("enter the elements:")
for i in range(n):
    element=int(input(f"Element{i+1:}"))
    array.append(element)

sum=0
for i in array:
    sum=sum+i
print("the sum of array is:",sum)

if (n>0):
    average=sum/n
else:
    average=0
print("the average of array is:",average)

