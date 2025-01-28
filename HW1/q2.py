 

age = int(input("What is your age?\n"))

print("You are", age, "years old.\n")
older = age+5
print("In 5 years you will be", older)

file = open("q2.out","w")
file.write("Age: " + str(age) + "\nAge+5: " + str(older))
file.close()