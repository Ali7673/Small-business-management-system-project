from data import employees
def SearchEmployee():
    print("Searching for an employee...")
    # Code to search for an employee goes here
    employee_id = int(input("Enter the employee ID to search for: "))
    for emp in employees:
        if emp["id"] == employee_id:
            print(f"Employee found - ID: {emp['id']}\n, Name: {emp['name']}\n, Age: {emp['age']}\n, Role: {emp['role']}\n, Salary: {emp['salary']}\n")