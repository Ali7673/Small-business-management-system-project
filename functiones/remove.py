from data import employees

def RemoveEmployee():
    print("Removing an employee...")
    # Code to remove an employee goes here
    employee_to_remove = int(input("Enter the ID of the employee to remove: "))
    for emp in employees:
        if emp["id"] == employee_to_remove:
                employees.remove(emp)
                print(f"Employee with ID {employee_to_remove} has been removed.")
                break

