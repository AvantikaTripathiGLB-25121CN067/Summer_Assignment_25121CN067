n=int(input('n'))
decimal=0
power=0
while n>0:
    d=n%10
    decimal+=(d*(2**power))
    n//=10
    power+=1
print(decimal)
