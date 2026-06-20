rows=int(input("enter the number of rows:"))
cols=int(input("enter the number of columns:"))

print("enter the elements of matrix a:")
matrix_a=[[int(input(f"a[{i}][{j}]:")) for j in range(cols)] for i in range(rows)]

print("enter the elements of matrix b:")
matrix_b=[[int(input(f"b[{i}][{j}]:")) for j in range(cols)] for i in range(rows)]

result=[[0 for _ in range(cols)]for _ in range(rows)]

for i in range(len(matrix_a)):
    for j in range(len(matrix_b[0])):
        for k in range(len(matrix_b)):
            result[i][j] +=matrix_a[i][k]*matrix_b[k][j]

for r in result:
    print (r)
