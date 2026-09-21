from lis import names, grades, add_student                #search/show, imports from File 1

def show_all():
    for i in range(len(names)):
        print(names[i], "-", grades[i])

def search(name):
    if name in names:
        index = names.index(name)
        print(grades[index])
    else:
        print("not found")

show_all()
search("sandip")