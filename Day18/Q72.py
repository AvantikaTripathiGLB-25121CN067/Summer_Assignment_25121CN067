arr=[int(x) for x in input("enter the values").split()]

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]<arr[j]:
            arr[i],arr[j]=arr[j],arr[i]

print("array in descending order:",arr)