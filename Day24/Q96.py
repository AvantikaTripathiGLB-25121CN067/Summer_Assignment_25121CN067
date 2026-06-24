text=input("enter a string:")
result=""

for char in text:
    if char not in result:
        result+=char

print("string after removing duplicates:",result)