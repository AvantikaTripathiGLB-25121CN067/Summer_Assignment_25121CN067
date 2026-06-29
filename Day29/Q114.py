class ArrayManager:
    def __init__(self): self.arr=[]
    def insert(self,val): self.arr.append(val)
    def remove(self,val): self.arr.remove(val) if val in self.arr else print("Not found")
    def display(self): print("Array:",self.arr)

ar= ArrayManager()

while True:
    print("\n 1.Insert 2.Remove 3.Display 4.Exit")

    ch=input("Choice:")

    if ch=='1': ar.insert(input("Value:"))

    elif ch=='2': ar.remove(input("Value:"))

    elif ch=='3': ar.display()

    elif ch=='4': break
    