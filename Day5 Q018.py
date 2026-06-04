n=int(input('n'))
num=n
factorial_sum=0
while n>0:
    digit=n%10
    
    fac=1
    for i in range(1,digit+1):
        fac*=i
    factorial_sum+=fac
    n//=10
if(factorial_sum==num):
    print('strong number')
else:
    print('no strong number')
    
