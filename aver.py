class Student():
 def __init__(self,name,grade):
    self.name = name
    self.grade = grade
 def average_above(students,target):
    a = 0
    for s in students:
        if s.grade> target:
            a = a+1
    return a
s1 = Student("sahil", 45)
s2 = Student("sandip", 87)
s3 = Student("sajan", 65)
students = [s1,s2,s3]
print(Student.average_above(students,23))