n=int(input("enter the number of elements:"))
array=[]
print("enter the elements:")
for i in range(n):
    element=input(f"Elements{i+1:}")
    array.append(element)

if n>0:
    smallest=array[0]
    largest=array[0]
    for i in array:
        if i<smallest:
            smallest=i
        if i>largest:
            largest=i

    print("the smallest element is:",smallest)
    print("the largest element is:",largest)