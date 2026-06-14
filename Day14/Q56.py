n=int(input("enter the number of elements:"))
array=[]
print("enter the elements:")
for i in range(n):
    element=int(input())
    array.append(element)

duplicates=[]

for i in range(len(array)):
    for j in range(i+1,len(array)):
        if array[i]==array[j]:
            already_added=False
            for d in duplicates:
                if d==array[i]:
                    already_added=True

            if not already_added:
                duplicates.append(array[i])
print("the duplicate elements are:", duplicates)