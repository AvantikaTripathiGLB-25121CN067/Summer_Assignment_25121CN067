arr=[int(x) for x in input("enter the values").split()]
n=len(arr)

for i in range (n):
    for j in range(0,n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]

print("sorted array using bubble sort:",arr)