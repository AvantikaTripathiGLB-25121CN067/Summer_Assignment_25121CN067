arr1=input("enter the values:").split()
arr2=input("enter the values:").split()
intersection=[]

for i in range(len(arr1)):
    for j in range(len(arr2)):
        if arr1[i]==arr2[j]:
            exists=False

            for k in range(len(intersection)):
                if arr1[i]==intersection[k]:
                    exists=True
                    break
            if not exists:
                intersection+=[arr1[i]]

print(intersection)