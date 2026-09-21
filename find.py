class Student():
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def show(self):
        print(self.name, "-", self.grade)

    def is_passing(self):
        return self.grade >= 50


def find_and_check(students, name):
    found = False                          # assume not found until proven otherwise
    for s in students:                     # check every student in the list
        if s.name == name:                 # does this student's name match?
            found = True                   # yes -> flip the flag
            if s.grade >= 50:
                print(s.name, "-", s.grade, "-", "passing")
            else:
                print(s.name, "-", s.grade, "-", "fail")
    if found == False:                     # AFTER checking everyone, still not found?
        print("Student not found")


s1 = Student("sahil", 45)
s2 = Student("sandip", 87)
s3 = Student("sajan", 65)
students = [s1, s2, s3]

find_and_check(students, "sajan")          # should print: sajan - 65 - passing
find_and_check(students, "unknown_name")   # should print: Student not found
