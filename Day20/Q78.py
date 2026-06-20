rows=int(input("enter the number of rows:"))
cols=int(input("enter the number of columns:"))

print("enter the elements of matrix a:")
matrix_a=[[int(input(f"a[{i}][{j}]:")) for j in range(cols)] for i in range(rows)]

is_symmetric=True

for i in range(rows):
    for j in range(cols):
        if matrix_a[i][j]!=matrix_a[j][i]:
            is_symmetric=False
            break

if is_symmetric:
    print("the matrix is symmetric")
else:
    print("the matrix is not symmetric")
        
