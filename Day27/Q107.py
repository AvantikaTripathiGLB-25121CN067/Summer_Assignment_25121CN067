class SalaryRecord:
    def __init__(self,emp_id,basic_salary):
        self.emp_id=emp_id
        self.basic_salary=basic_salary

    def calculate_net_salary(self):
        tax=self.basic_salary*0.10
        return self.basic_salary-tax
    
class SalaryManagement:
    def __init__(self):
        self.records=[]

    def add_records(self,emp_id,salary):
        self.records.append(SalaryRecord(emp_id,salary)) 

    def generate_payroll(self):
        print("\n---Monthly Payroll---")
        for r in self.records:
            print(f"Emp id:{r.emp_id} | Net pay: ${r.calculate_net_salary() }")

sal=SalaryManagement()
sal.add_records("E005",50000)
sal.add_records("E009",60000)
sal.generate_payroll( ) 
    