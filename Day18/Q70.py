arr=[int(x) for x in input("enter the values").split()]
n=len(arr)

for i in range(n):
    min_index=i
    for j in range(i+1,n):
        if arr[j]<arr[min_index]:
            min_index=j

    arr[i],arr[min_index]=arr[min_index],arr[i]

print("sorted array using selection sort:",arr)