rows = 5
i = 1

while i <= rows:
    
    spaces = 1
    while spaces <= (rows - i) * 2:
        print(" ", end="")
        spaces += 1
        
    
    j = 0
    while j < i:
        
        print(chr(65 + j), end=" ")
        j += 1
        
    
    j = i - 2
    while j >= 0:
        print(chr(65 + j), end=" ")
        j -= 1
        
    
    print()
    i += 1
