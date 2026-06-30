employees=[]

def add_employee(emp_id,name,departement):

    """Adds a new employee record."""
    employee={
        'id':emp_id,
        'name':name,
        'dept':departement
    }

    employees.append(employee)
    print(f"Added: {name}")

def remove_employee(emp_id):

    """Removes an employee by their ID."""
    global employees
    employees= [emp for emp in employees if emp ['id'] !=emp_id ]
     
    print(f"Removed employee with ID: {emp_id}")

def display_employees():

    """Displays all employee records."""
    print("\n--- Current Employee List---")

    if not employees:
        print("No records found.")
    for emp in employees:
        print(f"ID:{emp['id']}  Name:{emp['name']}  Department:{emp['dept']}")
    print("-------\n")

add_employee(101,"Alice","HR")
add_employee(102,"Bob","IT")
add_employee(103,"Charlie","Finance")

display_employees()

remove_employee(102)
display_employees()