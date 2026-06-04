def sum_of_digits(n):
    number=abs(n)
    total=0
    
    while (number>0):
        d=number%10
        total=total+d
        number//=10
        
    return total
n=int(input('n'))
print(sum_of_digits(n))