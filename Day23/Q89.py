text=input("enter a string:")

char_counts={}

for char in text:
    if char in char_counts:
        char_counts[char]+=1
    else:
        char_counts[char]=1

found=False
for char in text:
    if char in text:
        if char_counts[char] ==1:
            print(f"first non repeating character:{char}")
            found=True
            break

if not found:
    print("no non repeating character found.")