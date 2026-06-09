def armstrong(n):
    if(n<0):
        return'no result'
    else:
        original=n
        sum=0
        while(n>0):
            d=n%10
            sum+=d**3
            n//=10
        return original==sum
n=int(input('n'))
print(armstrong(n))