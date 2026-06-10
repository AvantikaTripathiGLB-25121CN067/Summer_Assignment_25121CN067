def palindrome(n):
    if(n<0):
        return'no result'
    else:
        original=n
        reversed=0
        while(n>0):
            d=n%10
            reversed=reversed*10+d
            n//=10
        return original==reversed
n=int(input('n:'))
print(palindrome(n))
