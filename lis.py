names=[]                            #program forholds the lists + add/remove.
grades=[]
def add_student(name,grade):
    names.append(name)
    grades.append(grade)

def remove(name):
    if name in names:
        index=names.index(name)
        names.pop(index)
        grades.pop(index)
    else:
        print(name,"not found")
add_student("sahil", 45)
add_student("sandip", 34)
remove("sahil")       #add_student(name,student) needed if the file is alone and data should   be here