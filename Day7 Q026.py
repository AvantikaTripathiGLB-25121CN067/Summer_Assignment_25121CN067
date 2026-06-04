def fibonacci(n):
    a=0
    b=1
    sequence=''
    if (n>0):
        
        for i in range(n):
         print(a)
         a,b=b,a+b
    elif(n<0):
        for i in range(abs(n)):
            print(a)
            a,b=b,a-b
    else:
        sequence=0
        
    return sequence
   
n=int(input('n'))
print(fibonacci(n))