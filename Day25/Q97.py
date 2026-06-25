arr1=[int(x) for x in input("enter the values:").split()]
arr2=[int(x) for x in input("enter the values:").split()]
merged=[]
 
i=0
j=0

while i <len(arr1) and j<len(arr2):
    if arr1[i]<arr2[j]:
        merged.append(arr1[i])
        i+=1
    else:
        merged.append(arr2[j])
        j+=1

merged.extend(arr1[i:])
merged.extend(arr2[j:])

print("merged array:",merged)
