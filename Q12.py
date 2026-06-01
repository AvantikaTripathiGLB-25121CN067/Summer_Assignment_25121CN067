a=int(input('a'))
b=int(input('b'))
if (a>b):
    n=a
else:
    n=b
    while True:
        if (n%a==0) and (n%b==0):
            lcm=n
            break
        n+=1
       
print(lcm)