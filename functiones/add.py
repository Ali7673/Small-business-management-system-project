from data import employees

def AddEmployee():
    print("Adding an employee...")
    # Code to add an employee goes here
    new_id = max([emp['id'] for emp in employees], default=0) + 1
    print (f"Assigned Employee ID: {new_id}")
    name = input("Enter employee name: ")
    age = input("Enter employee age: ")
    role = input("Enter employee role: ")
    salary = input("Enter employee salary: ")
    new_employee = {
        "id": new_id,
        "name": name,
        "age": age,
        "role": role,
        "salary": salary
    }
    employees.append(new_employee)
    print(f"Employee {name} added successfully with ID {new_id}.")