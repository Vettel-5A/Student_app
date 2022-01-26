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
        self.classes[period] = {teacher:None}

    def add_grade(self, teacher,grade):
        for value in self.classes.values():
            for point in value.keys():
                try:
                    if point == teacher:
                        value[point] = int(grade)

                    else: 
                        pass

                except TypeError:
                    pass

    @classmethod
    def add_student(cls, student):
        cls.students.append(student)




    
