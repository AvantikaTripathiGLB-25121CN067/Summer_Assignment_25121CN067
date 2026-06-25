names=input("enter a list of names:").split()

n=len(names)

for i in range(n):
    for j in range(0,n-i-1):
        if names[j].lower()>names[j+1].lower():

            names[j],names[j+1]=names[j+1],names[j]

print("sorted names:",names)


