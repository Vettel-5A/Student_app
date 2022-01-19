class Student:
    students = []
    def __init__(self, school, grade, fname, lname, gpa):
        self.school = school
        self.grade = grade
        self.fname = fname
        self.lname = lname
        self.classes = {}
        self.gpa = gpa


    def add_classes(self, period, teacher):
        self.classes[period] = teacher

    @classmethod
    def add_student(cls, student):
        cls.students.append(student)





    
