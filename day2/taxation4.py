'''
Level 4: Net Salary Calculation
Objective: Calculate annual net salary after tax deductions.
Tasks:
1. Compute Net Salary = Annual Gross Salary - Total Tax Payable.
2. Display:
o Annual Gross Salary
o Total Tax Payable (including cess)
o Annual Net Salary
'''

import taxation3 as t3, taxation as t1

net_annual_salary = t1.annual_gross_salary - t3.total_tax_amount
print(f'Annual Gross Salary = {t1.annual_gross_salary}')
print(f'Total Tax Amount = {t3.total_tax_amount}')
print(f'Net Annual Salary = {net_annual_salary}')