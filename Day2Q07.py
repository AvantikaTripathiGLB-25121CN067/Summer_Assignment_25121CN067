n=int(input('n'))
product=1
while n>0:
    d=n%10
    product=product*d
    n//=10
    print(product)
