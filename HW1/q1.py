
name = str(input("What is your name?\n")).capitalize()

print("Hello,", name)

file = open("q1.out", "w")
file.write("Hello, " + name)
file.close()

