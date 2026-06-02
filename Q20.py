n=int(input('n'))
if(n<2):
    print('no prime factor')
else:
    factor=2
    while(factor*factor<n):
        if(n%factor==0):
            n//=factor
        else:
            factor+=1
        print(n)