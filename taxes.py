#user enters income, PY calculates tax to pay, print result

print("Welcome to the Tax Calculator!")

income = float(input("Please Enter Your Annual Income: "))

tax = income / 20

print(F"With an Income of £{income}0, Your tax for the year is £{tax}0.")