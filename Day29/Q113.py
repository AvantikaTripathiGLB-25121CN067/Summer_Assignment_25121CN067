class Calculator:
    def add(self,a,b): return a+b
    def subtract(self,a,b): return a-b
    def multiply(self,a,b): return a*b
    def division(self,a,b): return a/b

calc=Calculator()

while True:
    print("\n 1.Add 2.Subtract 3.Multiply 4.Division 5.Exit")

    choice=input("Choice:")
    if choice =='5':break

    x,y=float(input("Num1:")),float(input("Num2:"))

    if choice=='1': print("Result:",calc.add(x,y))
    elif choice=='2': print("Result:",calc.subtract(x,y))
    elif choice== '3': print("Result:",calc.multiply(x,y))
    elif choice== '4': print("Result:",calc.division(x,y))