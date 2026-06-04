lower_range=300
upper_range=400
print('Armstrong number between lower and upper+1')
for num in range(lower_range,upper_range+1):
    digits=str(num)
    power=len(digits)
    total=sum(int(digit)**power for digit in digits)
    if total==num:
        print(num)
