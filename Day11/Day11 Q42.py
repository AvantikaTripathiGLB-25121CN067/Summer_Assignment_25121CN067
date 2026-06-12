def maximum(n):
    if not n:
        return None
    max_val=n[0]
    for num in n:
        if num > max_val:
            max_val=num
    return max_val
    
num=[10,63,92,2,93]
print(maximum(num))
    