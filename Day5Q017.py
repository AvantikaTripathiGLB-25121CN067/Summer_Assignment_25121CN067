n=int(input('n'))
if n<=0:
    print('no result')
else:
    sum_of_divisors=0
    for i in range(1,n):
        if(n%i==0):
            sum_of_divisors+=i
if (sum_of_divisors==n):
    print('perfect number')
else:
    print('no perfect number')
