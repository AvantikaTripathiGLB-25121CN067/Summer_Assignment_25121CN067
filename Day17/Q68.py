arr1=input("enter the values").split()
arr2=input("enter the values").split()
common=[]

for i in range(len(arr1)):
    for j in range(len(arr2)):
        if arr1[i]==arr2[j] and arr1[i] is not common:
            common.append(arr1[i])

print(common)