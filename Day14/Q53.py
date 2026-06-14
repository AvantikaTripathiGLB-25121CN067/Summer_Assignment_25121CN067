n=int(input("enter the number of elements:"))
array=[]
print("enter the elements:")
for i in range(n):
    element=int(input())
    array.append(element)

target=int(input("enter the target element:"))
result_index=-1
for i in range(len(array)):
        if array[i]==target:
            result_index=i
            break
print("Index:",result_index)
