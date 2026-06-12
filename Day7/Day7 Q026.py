def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    if n<0:
        pos_n=abs(n)
        if pos_n%2==1:
            return -fibonacci(pos_n)
        else: 
            return fibonacci(pos_n)
    return fibonacci(n-1)+fibonacci(n-2)
n=int(input("enter the number:"))
print(f"the {n}th term of the Fibonacci sequence is: {fibonacci(n)}")       

        
            
