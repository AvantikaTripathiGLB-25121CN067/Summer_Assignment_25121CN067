num = int(input('num'))
count = 0
if num == 0:
    count = 1
else:
    
    temp = abs(num)
       
while temp > 0:
        
        temp //= 10  
        count += 1   

print(count)
