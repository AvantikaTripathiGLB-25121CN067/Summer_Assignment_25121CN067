rows=int(input("enter the number of rows:"))
cols=int(input("enter the number of columns:"))

print("enter the elements of matrix:")
matrix=[[int(input(f"[{i}][{j}]:")) for j in range(cols) ] for i in range(rows)]

diag_sum=0
for i in range(rows):
    diag_sum +=matrix[i][i]

for r in matrix:
    print(r)
    
print(diag_sum)