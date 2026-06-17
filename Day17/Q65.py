array1=input("enter the values separated by spaces:").split()
array2=input("enter the values separated by spaces:").split()

merged=[]

for i in range(len(array1)):
    merged+=[array1[i]]

for i in range(len(array2)):
    merged+=[array2[i]]

print("Merged array:",merged)