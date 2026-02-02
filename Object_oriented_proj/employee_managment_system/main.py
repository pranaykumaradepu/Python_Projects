class Employee:
    employee_prefix = 'AB00'
    def __init__(self, employee_name, employee_salary):
        # We use the global employees list to determine the next ID number
        self.employee_id = f"{Employee.employee_prefix}{len(employees) + 1}"
        self.employee_name = employee_name
        self.employee_salary = employee_salary

    def display_details(self):
        print('\n---- Employee Details ---')
        print(f'Employee ID : {self.employee_id}')
        print(f'Employee Name : {self.employee_name}')   
        print(f'Employee salary : {self.employee_salary}') 
    
    def calculate_bonus(self):
        return self.employee_salary * 0.1


class Manager(Employee):
    def __init__(self, employee_name, employee_salary,department):
        super().__init__( employee_name, employee_salary)
        self.department = department
    
    def display_details(self):
        super().display_details()
        print(f'Manager Department : {self.department}')
    
    def calculate_bonus(self):
        return super().calculate_bonus() * 0.3
    

class Developers(Employee):
    def __init__(self, employee_name, employee_salary, programming_language):
        super().__init__( employee_name, employee_salary)
        self.programming_language = programming_language
    
    def display_details(self):
        super().display_details()
        print(f'Programming Language : {self.programming_language}')

    def calculate_bonus(self):
        return super().calculate_bonus() * 0.15

# main program 

employees = []

def create_employee():
    print('\nselect type of employee : ')
    print('1. Standard Employee')
    print('2. Manager')
    print('3. Developer')
    try:
        choice = int(input('Enter your choice (1-3): '))
        name = input('Enter employee name: ')
        salary = float(input('Enter employee salary: '))
        
        if choice == 1:
            employees.append(Employee(name, salary))
        elif choice == 2:
            department = input('Enter manager department: ')
            employees.append(Manager(name, salary, department))
        elif choice == 3:
            programing_language = input('Enter programming language: ')
            employees.append(Developers(name, salary, programing_language))
        else:
            print('invalid choice')
    except ValueError:
        print('Invalid Input. Please enter numbers for choice and salary.')

    

def display_all_employees(employees):
    if not employees:
        print('\nNo employees found')
        return
    for employee in employees:
        employee.display_details()
        print(f'Bonus : {employee.calculate_bonus():.2f}')

while True:
    print(f'\n--- Employee Managment system ----')
    print('1. Create Employee')
    print('2. View All Employees')
    print('3. Exit')

    try:

        choice = int(input('Enter your choice (1-3): '))

        if choice == 1:
            create_employee()
        elif choice == 2:
            display_all_employees(employees)
        elif choice == 3:
            print('Exiting the application')
            break
        else:
            print('Invalid choice. Please enter a number between 1 and 3.')
        
    except ValueError:
        print('Invalid input. Please enter a number.')


