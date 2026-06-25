str1=input("enter first string:")
str2=input("enter second string:")

common=[]

for char in set(str1):
    if char in str2:
        common.append(char)

print("common characters:",common)