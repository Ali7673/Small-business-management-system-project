from data import employees
def UpdateEmployee():
    print("Updating an employee's salary...")
    # Code to update an employee's salary goes here
    employee_id = int(input("Enter the employee ID to update: "))
    new_salary = float(input("Enter the new salary: "))
    for emp in employees:
        if emp["id"] == employee_id:
            emp["salary"] = new_salary
            print(f"Employee ID {employee_id} salary updated to {new_salary}.")
            break