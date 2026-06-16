n=int(input("enter the number of elements"))
arr=[]
print("enter the elements")
for i in range(n):
    element=int(input())
    arr.append(element)

target=50

found=False
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==target:
            print(f"pair found:({arr[i]},{arr[j]})")
            found=True

if not found:
    print("no pair found")