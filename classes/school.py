from classes.student import Student
from classes.staff import Staff
# school.py
class School:
    def __init__(self, name):
        self.name = name
        #uses the class method to create the list from the
        #imported .csv file
        self.staff = Staff.all_staff()
        self.students = Student.all_students()