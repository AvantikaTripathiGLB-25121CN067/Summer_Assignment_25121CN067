size=5
i=0
while i<size:
    if i==0 or i==size-1:
        print('*'  * size)
    else:
        print('*'+' '*(size-2)+'*')
    i+=1