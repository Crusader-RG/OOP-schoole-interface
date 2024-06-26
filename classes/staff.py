#staff.py
import csv

class Staff:
    def __init__(self, name, age, role, employee_id, password):
        self.name = name 
        self.age = age         
        self.password = password
        self.role = role
        self.employee_id = employee_id

    @classmethod
    def all_staff(cls):
        staff = []
        with open('./data/staff.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                new_staff = cls(**row)
                staff.append(new_staff)
        # print(staff)
        return staff
    


