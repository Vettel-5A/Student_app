from student import Student
import tutorial
from flask import Flask

def main():

    student1 = Student("Leland", 9, "Arnav", "Vajirkar", 4.0)
    Student.add_student(student1)
    student1.add_classes(1, "Sarkar")
    student1.add_classes(2, "Yen")

    print(tutorial.get_tutorial(student1, "Friday"))

    

if __name__ == '__main__':
    main()
