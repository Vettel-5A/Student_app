import pandas as pd
import openpyxl
import numpy

class Student:
    students = []
    def __init__(self, school, grade, fname, lname):
        self.school = school
        self.grade = grade
        self.fname = fname
        self.lname = lname
        self.classes = {1:"Sarkar"}


    def add_classes(self, period, teacher):
        self.classes[period] = teacher

    @classmethod
    def add_student(cls, student):
        cls.students.append(student)

student1 = Student("Leland", 9, "Arnav", "Vajirkar")
Student.add_student(student1)
student1.add_classes(2, "Yen")


data = "School.csv"
df = pd.read_csv(data)

df.set_index("Name", inplace=True)

open_teachers = []
def get_tutorial(student, day):
    for period in student.classes:
        if str(df.loc[student.classes[period], day]) == "open": #line doesnt update after first time so that needs fixing
            open_teachers.append(student.classes[period])



get_tutorial(student1, "Wenesday")
print(open_teachers)








