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
while True:
    print('---------------------------------------')
    print('1. Add students and subjects\n2. Show subjects by student name\n3. Show students by subject\n4. Show all')
    option = int(input('Please, choose an option: '))
    if option == 1:
        num_of_students = int(input("Write number of students: "))
        for i in range(num_of_students):
            name = input(f"Name of {i+1} student: ")
            subjects = input(f"Subjects of {i+1} student: ").split()
            students[name] = subjects
    elif option == 2:
        name_of_student = input('Enter the name of student to see the list of subjects: ')
        print(student_for_sub(name_of_student))
    elif option == 3:
        subject = input('Enter the subject to see the list of students: ')
        print(sub_for_students(subject))
    elif option == 4:          
        print(show_all())
    else:
        print('Please, enter the right option')

    

    
