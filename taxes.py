#user enters income, PY calculates tax to pay, print result

print("Welcome to the Tax Calculator!")

income = input("Please Enter Your Annual Income: ")

tax = float(income) / 20

print(F"With an Income of £{income}, Your tax for the year is £{tax}0.")