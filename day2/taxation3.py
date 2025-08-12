'''Level 3: Tax and Rebate Calculation
Objective: Compute tax payable using the New Tax Regime (2023) slabs.
Tasks:
1. Calculate tax based on the following slabs:
o ₹0 - ₹3,00,000: 0%
o ₹3,00,001 - ₹6,00,000: 5%
o ₹6,00,001 - ₹9,00,000: 10%
o ₹9,00,001 - ₹12,00,000: 15%
o ₹12,00,001 - ₹15,00,000: 20%
o Above ₹15,00,000: 30%
2. Apply Section 87A Rebate:
o Taxable income ≤ ₹7,00,000 → 100% rebate (tax payable = ₹0).
3. Add a 4% Health and Education Cess to the calculated tax.
Output:
• Display a detailed tax breakdown, including slabs, cess, and total tax payable.
----------------------------------------
'''

import taxation2


if taxation2.taxable_income >=300000:
    print('The tax you nee to pay is 0% ')
elif 300001<=taxation2.taxable_income >=600000:
    print('The tax you nee to pay is 5% ') 
elif 600001<=taxation2.taxable_income >=900000:
    print('The tax you nee to pay is 10%')
elif 900001<=taxation2.taxable_income >=1200000:
    print('The tax you nee to pay is 15% ')
elif 1200001<=taxation2.taxable_income >=1500000:
    print('The tax you nee to pay is 20% ')
elif taxation2.taxable_income<1500000:
    print('The tax you nee to pay is 30% ')
else 