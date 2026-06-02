n=int(input('n'))
if n<0:
    print('no result')
else:
    for i in range(1,n):
        if(n%i==0):
            print(i)
        else:
            print('no result')
    