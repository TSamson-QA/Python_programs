print("Welcome to the Grade Calculator!")

mark = int(input("Please enter your final mark: "))

if mark >= 85:
    print("Congratulations! You got a distinction!")
elif mark > 65:
    print("Well done, you got a Pass!")
else:
    print("Unfortunately you failed, better luck next time.")


print("Welcome to the Grade Calculator!")

mark = int(input("Please enter your final mark: "))

if mark >= 85:
    print("Congratulations! You got a distinction!")
if mark > 65 and mark < 85:
    print("Well done, you got a Pass!")
if mark < 65:
    print("Unfortunately you failed, better luck next time.")