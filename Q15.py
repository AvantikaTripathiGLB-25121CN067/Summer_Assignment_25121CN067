digits='370'
power=len(digits)

total =sum(int(digit)**power for digit in digits)
print(total)