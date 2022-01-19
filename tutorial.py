import pandas as pd
from student import Student

def get_tutorial(student, day):
    open_teachers = []
    data = "School.csv" 
    df = pd.read_csv(data) #reads csv into dataframe

    df.set_index("Name", inplace=True) #Makes name attribute the way to index rows

    """Loops Through every period in classes dictionary.
    Gets name of each teacher. Indexes that row and column for day passed in.
    Checks if that slot is open, and if so adds it as an open teacher"""
    
    for period in student.classes: 
        if str(df.loc[student.classes[period]].loc[day]) == "open": #gets teacher and day slot in csv and checks whether open or not
            open_teachers.append(student.classes[period])

    return open_teachers








