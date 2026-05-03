header = "===== COMPANY SYSTEM ====="
footer = "=========================="
functiones = "1- Add Employee\n2- Remove Employee\n3- Show All Employees\n4- Search Employee\n5- Update Employee Salary\n6- Company Statistics\n7- Exit"
print(header)
print(functiones)
print(footer)
choise = input("Please select a function: ")

while choise != "7":
    if choise == "1":
            print("You selected: Add Employee\nknow you can add an employee to the system.")

    elif choise == "2":
            print("You selected: Remove Employee\nknow you can remove an employee from the system.")
        
    elif choise == "3":
            print("You selected: Show All Employees\nknow you can show all employees in the system.")
        
    elif choise == "4":
            print("You selected: Search Employee\nknow you can search for an employee in the system.")
        
    elif choise == "5":
            print("You selected: Update Employee Salary\nknow you can update an employee's salary in the system.")
        
    elif choise == "6":
            print("You selected: Company Statistics\nknow you can view company statistics.")
        
    elif choise == "7":
            print("You selected: Exit\nThank you for using the Company System.")
        
    else:   print("Invalid selection. Please select a valid function from the menu.")


    print(header)
    print(functiones)
    print(footer)
    choise = input("Please select a function: ")

else:    print("You selected: Exit\nThank you for using the Company System.")