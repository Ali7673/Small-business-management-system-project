from data import employees
def CompanyStatistics():
    print("Calculating company statistics...")
    # Code to calculate and display company statistics goes here
    total_employees = len(employees)
    if total_employees > 0:
        average_salary = sum(emp["salary"] for emp in employees) / total_employees
        print(f"Total Employees: {total_employees}")
        print(f"Average Salary: {average_salary:.2f}")
    else:
        print("No employees found to calculate statistics.")