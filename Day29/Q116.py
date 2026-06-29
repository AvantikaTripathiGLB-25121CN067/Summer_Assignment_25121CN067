class Inventory:
    def __init__(self): self.stock={}
    def add_item(self,name,qty):self.stock[name]=self.stock.get(name,0)+qty
    def view_stock(self):
        for item,qty in self.stock.items(): print(f"{item}:{qty}")

inv=Inventory()

while True:
    print("\n 1.Add item 2.View stock 3.Exit")

    ch=input("Choice:")
    if ch=='1':
        inv.add_item(input("Item:"),int(input("Quantity:")))
    elif ch=='2': inv.view_stock()
    elif ch=='3': break