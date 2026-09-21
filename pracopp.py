class Student():
    def __init__(self,name,grade):
        self.name = name 
        self.grade = grade  

    def show(self):
        print(self.name,"-",self.name)

    def is_passing(self):
        return self.grade >= 50

    def average(students):
        sum=0
        for i in students:
         sum = i.grade +sum
        av = sum / len(students)
        return av
    def pass_s(students):
         for i in students:
             if i.grade >= 50:
                print(i.name,"-",i.grade) 
s1 = Student("sahil",47)
s2 = Student("sandip",88)
print(s1.is_passing())
print(s2.is_passing())
students=[s1,s2]
result = Student.average(students)
pas = Student.pass_s(students)
print(result)
print(pas)