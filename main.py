from functiones import add, remove, allEmployee, search, update, stat


criteria = ["id", "name", "age", "role", "salary"]
employees = dict.fromkeys(criteria)




header = "===== COMPANY SYSTEM ====="
footer = "=========================="
functiones = "1- Add Employee\n2- Remove Employee\n3- Show All Employees\n4- Search Employee\n5- Update Employee Salary\n6- Company Statistics\n7- Exit"

print(header)
print(functiones)
print(footer)

choise = input("Please select a function: ")

while choise != "7":
    if choise == "1":
            add.AddEmployee()

    elif choise == "2":
            remove.RemoveEmployee()
        
    elif choise == "3":
            allEmployee.ShowAllEmployees()
        
    elif choise == "4":
            search.SearchEmployee()
        
    elif choise == "5":
            update.UpdateEmployee()
    elif choise == "6":
            stat.CompanyStatistics()
        
    elif choise == "7":
            quit.Quit()
        
    else:   print("Invalid selection. Please select a valid function from the menu.")


    print(header)
    print(functiones)
    print(footer)
    choise = input("Please select a function: ")

else:    print("You selected: Exit\nThank you for using the Company System.")