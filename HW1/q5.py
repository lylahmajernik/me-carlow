
studentList = []

cont = int(input("What would you like to do?\n1. Add student\n2. Exit\n"))


while cont != 10:
    if cont ==1:
        student = str(input("Enter student name.\n"))
        student = student.capitalize()
        studentList.append(student)
        cont = int(input("What would you like to do?\n1. Add another student\n2. Exit\n"))
    elif cont == 2:
        print("Goodbye")
        file = open('q5.out', 'w')
        for names in studentList:
            file.write(names +"\n")
        file.close()
        break
    else:
        print('invalid input.')