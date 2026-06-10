n=int(input("enter the number of elements:"))
user_array=[]
print("enter the elements:")
for i in range(n):
    element=input(f"Element {i+1}: ")
    user_array.append(element)
print("the array is:",user_array)

print("displaying elements:")
for i in user_array:
    print(i)