n=int(input('n'))
original=n
reverse=0
while n>0:
    d=n%10
    reverse=reverse*10+d
    n//=10
palindrome=(original==reverse)

print(palindrome)
    
    