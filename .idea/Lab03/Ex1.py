employee_salaries = {}

while True:
    employee_name = input("Enter the name of the employee (or 'print' to exit): ")
    
    if employee_name.lower() == 'print':
        break
    
    if not employee_name.isalpha():
        print("Invalid name input. Please enter only letters.")
        continue

    try:
        employee_salary = float(input("Enter the salary of {} : ".format(employee_name)))
    except ValueError:
        print("Invalid salary input. Please enter a numerical value.")
        continue
    
    employee_salaries[employee_name] = employee_salary

if not employee_salaries:
    print("No employees are present.")
else:
    print("\nEmployee Salaries:")
    for name, salary in employee_salaries.items():
        print("{}: ${:.2f}".format(name, salary))


