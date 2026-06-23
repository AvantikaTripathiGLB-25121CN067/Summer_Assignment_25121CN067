text=input("enter a string:")
max_char=""
max_count=0

for char in text:
    count=text.count(char)
    if count>max_count:
        max_count=count
        max_char=char

print(f"max occurring character is '{max_char}' ({max_count} times)")