rows=int(input("enter the number of rows:"))
cols=int(input("enter the number of columns:"))

print("enter the elements of matrix:")
matrix=[[int(input(f"[{i}][{j}]:")) for j in range(cols)]for i in range(rows)]

transpose=[[0 for _ in range (rows) ]for _ in range (cols)]

for i in range(rows):
    for j in range(cols):
        transpose[j][i]=matrix[i][j]

for r in transpose:
    print (r)