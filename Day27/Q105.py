class Student:
    def __init__(self,name,roll_no,age):
        self.name=name
        self.roll_no=roll_no
        self.age=age

class StudentManagement:
    def __init__(self):
        self.students={}

    def add_students(self,name,roll_no,age):
        self.students[roll_no]=Student(name,roll_no,age)
        print(f"Student {name} added successfully.")

    def display_all(self):
        print("\n----Student Records----")
        for s in self.students.values():
            print(f"Name:{s.name} |Roll no:{s.roll_no}| Age:{s.age}")

sms=StudentManagement()
sms.add_students("Rahul",55,16)
sms.add_students("Anjali",10,18)
sms.display_all()
