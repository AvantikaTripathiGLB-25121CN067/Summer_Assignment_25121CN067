n=int(input("n:"))
if n<0:
    print("no result")
else:
    original=n
    sum=0
    while n>0:
        digit=n%10
        sum+=digit**3
        n//=10
    if sum==original:
        print("Armstrong number")
    else:
        print("Not an Armstrong number")