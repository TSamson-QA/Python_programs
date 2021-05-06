'''
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

John = Student("John", "21")
Jane = Student("Jane", "22")

print(getattr(John, "age"))
'''

name_ = input("Please input name: ")
age_ = input("Please input age: ")
s_class = input("Please input class: ")
score_1 = int(input("Please enter score 1: "))
score_2 = int(input("Please enter score 2: "))
score_3 = int(input("Please enter score 3: "))
average_score = ""

def avg_test(score1, score2, score3):
    average_score = ((score1 + score2 + score3) / 3)
    return average_score

class Students:
    def __init__(self, name, age, class_, avg_score):
        self.name = name
        self.age = age
        self.class_ = class_ 
        self.avg_score = avg_score

average = avg_test(score_1, score_2, score_3)

Student1 = Students("Student", "Student", "Student", "Student")

setattr(Student1, "name", name_)
setattr(Student1, "age", age_)
setattr(Student1, "class_", s_class)
setattr(Student1, "avg_score", average)

print(getattr(Student1, "name"))
print(getattr(Student1, "age"))
print(getattr(Student1, "class_"))
print(getattr(Student1, "avg_score"))