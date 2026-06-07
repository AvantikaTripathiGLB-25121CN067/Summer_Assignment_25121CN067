rows = 5
i = 1

while i <= rows:
    
    spaces = 1
    while spaces <= (rows - i) * 2:
        print(" ", end="")
        spaces += 1
        
    
    j = i
    while j < (2 * i):
        print(j, end=" ")
        j += 1
        
    
    j = (2 * i) - 2
    while j >= i:
        print(j, end=" ")
        j -= 1
        
    
    print()
    i += 1
