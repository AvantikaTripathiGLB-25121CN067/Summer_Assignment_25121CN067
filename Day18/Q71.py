arr=[int(x) for x in input("enter the values").split()]
target=30
low=0
high=len(arr)-1
result=-1

while low<=high:
    mid=(low+high)//2
    if arr[mid]==target:
        result=mid
        break
    elif arr[mid]<target:
        low=mid+1
    else:
        high=mid-1

if result!= -1:
    print(f"element found:{result}")
else:
    print("element not found")