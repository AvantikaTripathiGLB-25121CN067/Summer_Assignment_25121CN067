class Employee:
    def __init__(self,emp_id,name,department):
        self.emp_id=emp_id
        self.name=name
        self.department=department

class EmployeeManagement:
    def __init__(self):
        self.employee={}

    def add_employee(self,emp_id,name,department):
        self.employee[emp_id]=Employee(emp_id,name,department)
        print(f"Employee {name} added successfully.")

    def display_all(self):
        print("\n---Employee Records---")
        for emp in self.employee.values():
            print(f"Employee id:{emp.emp_id} | Name:{emp.name} | Department:{emp.department}")

empy=EmployeeManagement()
empy.add_employee("E001","Arush","IT")
empy.add_employee("E002","Bella","Finance")
empy.display_all()