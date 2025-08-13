'''Level 1: Basic Input and Salary Calculation
Objective: Capture employee details and calculate the gross salary.
Tasks:
• Accept the following inputs for an employee:
o Name
o EmpID
o Basic Monthly Salary
o Special Allowances (Monthly)
o Bonus Percentage (Annual Bonus as % of Gross Salary)
• Calculate:
o Gross Monthly Salary = Basic Salary + Special Allowances
o Annual Gross Salary = (Gross Monthly Salary × 12) + Bonus
• Output:
o Display the employee details, gross monthly salary, and annual gross salary.
'''



emp_name = input('Enter your name:')
Emp_id = int(input('enter employee id: '))
monthly_salary = int(input('Enter your basic monthly salary: '))
s_allowance = int(input('enter your any special allowance (monthly): '))
bonus = int(input('enter your annual bonus in percentage: '))

g_monthly_salary = monthly_salary + s_allowance
annual_gross_salary = (g_monthly_salary  * 12)+(g_monthly_salary  * 12) *(bonus/100)


print(emp_name)
print(Emp_id)
print(monthly_salary)
print(s_allowance)
print(bonus)
print('The gross monthly salary is',g_monthly_salary)
print('The gross Annual salary is' , annual_gross_salary)