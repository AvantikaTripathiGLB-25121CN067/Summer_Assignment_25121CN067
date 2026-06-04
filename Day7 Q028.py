
def reverse(n, reversed=0):
    if n == 0:
        return reversed
        
    elif n < 0:
        
        num = abs(n)
        d = num % 10
        reversed = reversed * 10 + d
        num //= 10
        
        return -reverse(num, reversed)
        
    else:
        d = n % 10
        reversed = reversed * 10 + d
        n //= 10
        return reverse(n, reversed)

n = int(input('Enter n: '))
print(reverse(n))
