rows=int(input("enter the number of rows:"))
cols=int(input("enter the number of columns:"))

print("enter the elements of matrix a:")
matrix=[[int(input(f"[{i}][{j}]:")) for j in range(cols)] for i in range(rows)]

for j in range(cols):
    cols_sum=0
    for i in range(rows):
        cols_sum +=matrix[i][j]

print(cols_sum)