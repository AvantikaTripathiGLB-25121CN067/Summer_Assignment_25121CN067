def perfect_number(n):
    if(n<0):
        return 'no result'
    else:
        sum_of_divisors=0
        for i in range(1,n):
            if(n%i==0):
                sum_of_divisors+=i
        return sum_of_divisors==n
n=int(input('n:'))
print(perfect_number(n))