def sum_of_digits(n):
    n=abs(n)
    if n<10:
        return n
    last_digit=n%10
    remaining_digits=n//10
    return last_digit+sum_of_digits(remaining_digits)
n=int(input("enter the number:"))
print(f"the sum of the digits of {n} is: {sum_of_digits(n)}")