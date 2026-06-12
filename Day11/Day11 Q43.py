def prime(n):
    if (n<=1):
        return 'Composite'
    divisor=2
    while divisor*divisor<=n:
        if n%divisor==0:
            return 'Composite'
        divisor = divisor+1
    return 'Prime'
n=int(input('n'))
print(prime(n))