n = int(input('Enter the number of terms:'))    
a, b = 0, 1
for i in range(n):  
    a, b = b, a + b
print(a)