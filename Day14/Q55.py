n=int(input("enter the number of elements:"))
array=[]
print("enter the elements:")
for i in range(n):
    element=int(input())
    array.append(element)

largest=-999999
second_largest=-999999
for num in array:
    if num>largest:
        second_largest=largest
        largest=num
    elif num>second_largest and num!=largest:
        second_largest=num

print("the second largest element is:",second_largest)