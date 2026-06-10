n=int(input("enter the number of elements:"))
array=[]
print("enter the elements:")
for i in range(n):
    element=int(input(f"Element{i+1:}"))
    array.append(element)

even=0
odd=0
for i in array:
    if(i%2==0):
        even+=1
    else:
        odd+=1
print("the number of even elements is:",even)
print("the number of odd elements is:",odd)