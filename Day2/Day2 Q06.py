n = int(input('n'))

temp_n = abs(n)
reverse = 0

while temp_n > 0:
    d = temp_n % 10
    reverse = reverse * 10 + d
    temp_n //= 10

if n < 0:
    reverse = -reverse

print(reverse)
