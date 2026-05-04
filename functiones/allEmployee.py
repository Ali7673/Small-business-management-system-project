from data import employees
def ShowAllEmployees():
    print("Showing all employees...")
    # Code to show all employees goes here
    print ("ID\tName\tAge\tRole\tSalary")
    print("---------------------------------------------")
    for employee in employees:
        print(f"{employee['id']}\t{employee['name']}\t{employee['age']}\t{employee['role']}\t{employee['salary']}")