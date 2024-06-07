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

    def list_students(self):
        for idx, student in enumerate(self.students,1):
            print(f"{idx}. {student.name} {student.school_id}")

    def find_student_by_id(self, id):
        for student in self.students:
            if student.school_id == id:
                return student 
        print("Student does not exist")
        return None
            