class Student():                  #oop function knowledge.
    def __init__(self,name,grade):
        self.name =name
        self.grade =grade

    def show(self):
        print(self.name,"-",self.grade)

s1 = Student("sajan",45)
s2 = Student("sabin",76)    
s1.show()
s2.show() 

students=[]
def add_student(name,grade):
    students.append(Student(name,grade))
def show_all():
    for s in students   :   
        s.show()
add_student("Alice", 85)
show_all()