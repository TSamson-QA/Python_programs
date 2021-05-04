h_grade = 101
a_grade = 101
f_grade = 101

def grade_calc(h_score, a_score, f_score):
    final_grade = h_score + a_score + f_score
    return final_grade


while h_grade > 25:
    print("Please enter a valid score!")
    h_grade = int(input("Please input Homework Score out of 25: "))
    
while a_grade > 50:
    print("Please enter a valid score!")
    a_grade = int(input("Please input Assessment Score out of 50: "))
    
while f_grade > 100:
    print("Please enter a valid score!")
    f_grade = int(input("Please input Exam Score out of 100: "))
    
final = ((grade_calc(h_grade, a_grade, f_grade)) / 175) * 100

print("Final percentage score: ", int(final) , "%")

if final >= 90:
    print("Congratulations! You got a A*!")
elif final > 80:
    print("Well done, you got a A!")
elif final > 70:
    print("Well done, you got a B!")
elif final > 60:
    print("Well done, you got a C!")
else:
    print("Unfortunately you failed, better luck next time.")
