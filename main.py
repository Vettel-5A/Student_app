from student import Student
import tutorial
from numpy import interp
import pandas as pd
import time
import pickle
import os
from pathlib import Path

def main():
    student1 = Student("Leland", 9, "Arnav", "Vajirkar", 4.0)

    student2 = Student("Leland", 11, "Abhishek", "Kaushikkar", 3.68)
    Student.add_student(student1)
    student1.add_classes(1, "Sarkar")
    student1.add_classes(2, "Yen")
    student1.add_grade("Sarkar",4)
    print(student1.classes)

    print(tutorial.get_tutorial(student1, "Friday"))

    save_student(student1)
    delete_student(student2)

    
def save_student(student):
    student_name = str(student.lname)+".pickle"
    student_path = Path("/Users/abhi/Desktop/Student_App/students/"+student_name)

    if student_path.exists():
        try:
            with student_path.open('wb') as fp:
                pickle.dump(student, fp)

        except:
            pass

    else:
         with open(student_path,'wb') as fp:
            pickle.dump(student, fp)

def delete_student(student):
    student_name = str(student.lname)+".pickle"
    student_path = Path("/Users/abhi/Desktop/Student_App/students/"+student_name)
    if student_path.exists():
        try:
            os.remove(student_path)

        except:
            os.remove(student_name)
    else:
        print("no such student")
    


if __name__ == '__main__':
    main()



