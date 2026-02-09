#Task 3:
'''
Design a Python program using Object-Oriented Programming concepts with the following requirements:
Create a class Employee with:
Instance variables:
name
employee_id
basic_salary
Create a method calculate_salary() that:
Calculates the total salary by adding:
basic_salary
20% of basic salary as HRA
10% of basic salary as bonus
Returns the total salary
Create another method display_details() that prints:
Name: <name>
Employee ID: <employee_id>
Total Salary: <total_salary>
'''
class Employee:
    def __init__(self, name, employee_id, basic_salary):
        self.name = name
        self.employee_id = employee_id
        self.basic_salary = basic_salary

    def calculate_salary(self):
        hra = self.basic_salary * 0.20
        bonus = self.basic_salary * 0.10
        total_salary = self.basic_salary + hra + bonus
        return total_salary

    def display_details(self):
        total_salary = self.calculate_salary()
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Total Salary: {total_salary}")

emp = Employee("Sai", 101, 10000)
emp.display_details()
