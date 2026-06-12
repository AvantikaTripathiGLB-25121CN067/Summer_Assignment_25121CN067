def factorial(n):
    if n<0:
        return 'Undefined'
        
    fac=1
    
    for i in range(1,1+n):
           fac*=i
    return fac
   
n=int(input('n'))
print(factorial(n))
           