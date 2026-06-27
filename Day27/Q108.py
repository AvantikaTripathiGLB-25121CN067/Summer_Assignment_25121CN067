class Marksheet:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
        self.marks={}

    def get_marks(self):
        for sub in ["Maths","Science","English","Hindi"]:
            self.marks[sub]=int(input(f"enter {sub} marks:"))

    def show(self):
        total=sum(self.marks.values())
        percentage=total/len(self.marks)

        print(f"\n--- Marksheet for {self.name} (Roll:{self.roll_no})---")
        for sub,score in self.marks.items():
            print(f"{sub}:{score}")
        print(f"Total marks:{total} | Percentage:{percentage:.2f}%")

student=Marksheet(input("Name:"),input("Roll no:"))
student.get_marks()
student.show()