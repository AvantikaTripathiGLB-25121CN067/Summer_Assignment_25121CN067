n=int(input("enter the number of elements"))
arr=[]
print("enter the elements")
for i in range(n):
    element=int(input())
    arr.append(element)

unique_arr=[]

for i in range(len(arr)):
    duplicate=False
    for j in range(len(unique_arr)):
        if arr[i]==unique_arr[j]:
            duplicate=True
            break

    if not duplicate:
        unique_arr.append(arr[i])

print(unique_arr)


