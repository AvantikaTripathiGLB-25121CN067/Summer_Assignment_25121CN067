arr1=input("enter the values:").split()
arr2=input("enter the values:").split()
union=[]

for i in range(len(arr1)):
    union+=[arr1[i]]

for i in range(len(arr2)):
    exists=False
    for j in range(len(union)):
        if arr2[i]==union[j]:
            exists=True
            break
    if not exists:
        union+=[arr2[i]]

print(union)
        
     