

studentList = []

print("Type 'exit' at any time to exit")
student = str(input("Please enter a student you would like to add to the list.\n")).lower()


while student != 'exit':
    student = student.capitalize()
    studentList.append(student)
    student = str(input("List another student\n"))
    
    if student == "exit":
        print("Here's your list:\n",studentList)
        file = open('q4.out', 'w')
        for names in studentList:
            file.write(names +"\n")
        file.close()
        break