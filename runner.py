#because runner is same level as classes, we must direct it for all 3
from classes.school import School 
from classes.staff import Staff
from classes.student import Student

school = School('Ridgemont High') 

print(school.name)
print(school.students)
print(school.staff)