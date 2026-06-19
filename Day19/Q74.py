rows=int(input("enter number of rows:"))
cols=int(input("enter number of columns:"))

print("enter elements of matrix a:")
matrix_a=[[int(input(f"a[{i}][{j}]:"))for j in range(cols)] for i in range(rows)]

print("enter elements of matrix b:")
matrix_b=[[int(input(f"b[{i}][{j}]:")) for j in range(cols)] for i in range(rows)]

result=[[0 for _ in range(cols)] for _ in range(rows)]
for i in range(rows):
    for j in range(cols):
        result[i][j]=matrix_a[i][j]-matrix_b[i][j]

for r in result:
    print(r)

