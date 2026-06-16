n=int(input("enter the number of elements:"))
arr=[]
print(f"enter the {n-1} elements")
for i in range(n-1):
    element=int(input())
    arr.append(element)

min_val=min(arr)
max_val=max(arr)

expected_sum=((min_val+max_val)*n)//2

actual_sum=sum(arr)

missing_number=expected_sum-actual_sum
print(missing_number)