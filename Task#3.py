def show_all():
    res = ""
    for k, v in students.items():
        res += f"{k}: {v}\n"
    return res[:-1]

def student_for_sub(student_name):
    if student_name in students:
        return students[student_name]
    return "There are no students with this name"

def sub_for_students(subject):
    names = []
    flag = False
    for k, v in students.items():
        if subject in v:
            flag = True
            names.append(k)
    if not flag:
        return "There are no matching students."
    return names
            

students = {}
num_of_students = int(input("Write number of students: "))
for i in range(num_of_students):
    name = input(f"Name of {i+1} student: ")
    subjects = input(f"Subjects of {i+1} student: ").split()
    students[name] = subjects
    
print(show_all())