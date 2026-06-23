text=input("enter a string:")

seen={}
found=False

for char in text:
    if char in seen:
        print(f"first repeating character is:{char}")
        found=True
        break
    else:
        seen[char]=True

if not found:
    print("no repeating character found.")
