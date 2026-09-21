class student():
      def __init__(self,name,grade):
            self.name = name 
            self.grade = grade  
    
      def top_student(students):
       best = students[0]              # start by assuming the FIRST student is the best
       for s in students:                # check every student in the list
        if s.grade > best.grade:      # found someone better?
            best = s                  # update "best so far"
       return best.name                  # after checking everyone, return the winner's name
        
s1  = student("sahil",46)
s2 = student("sandip",76)
s3 = student("sajan",92)
s4 = student("sabin",74)
students = [s1,s2,s3,s4]
print(student.top_student(students))            