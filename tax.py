income = float(input("Please enter your income"))
dependants = int(input("Please enter the number of dependants"))
taxable_income = income - 10000 - 3000*dependants
tax = 0.2*taxable_income
print("Your income tax amount is ", tax)