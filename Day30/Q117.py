students=[]

def add_student(admission_no,name,roll_no):

    """Adds a  new student record."""
    student={
        'admission_no':admission_no,
        'name':name,
        'roll_no':roll_no
    }

    students.append(student)
    print(f"Added: {name}")

def remove_student(roll_no):

    """Removes an student by their roll_no."""
    global students
    students= [s for s in students if s ['roll_no'] !=roll_no ]
     
    print(f"Removed student with roll_no: {roll_no}")

def display_students():

    """Displays all student records."""
    print("\n--- Current Student List---")

    if not students:
        print("No records found.")
    for s in students:
        print(f"Admission_no:{s['admission_no']}  Name:{s['name']}  Roll_no:{s['roll_no']}")
    print("-------\n")

add_student(62087,"Ali",10)
add_student(63021,"Babita",15)
add_student(63052,"Chaitany",20)

display_students()

remove_student(15)
display_students()