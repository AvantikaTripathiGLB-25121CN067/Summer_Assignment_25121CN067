rows=int(input("enter the number of rows:"))
cols=int(input("enter the number of columns:"))

print("enter the elements of matrix a:")
matrix=[[int(input(f"[{i}][{j}]:")) for j in range(cols)] for i in range(rows)]

for i in range(rows):
    row_sum=0
    for j in range(cols):
        row_sum += matrix[i][j]

print(row_sum)