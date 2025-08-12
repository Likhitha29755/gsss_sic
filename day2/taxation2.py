import taxation
'''Level2:
Level 2: Taxable Income Calculation
Objective: Calculate taxable income after standard deductions.
Tasks:
• Deduct a Standard Deduction of ₹50,000 from the annual gross salary.
• Compute the Taxable Income and display all intermediate calculations.
Output: Display gross salary, standard deduction and taxable income.
'''


standard_deduction = 50_000
taxable_income = taxation.annual_gross_salary - standard_deduction
print(taxable_income)