


age = int(input("What is your age?\n"))


file = open("q3.out","w")

if age >= 20 and age <= 30:
    file.write("pass")
else:
    file.write("fail")
    
file.close()
    
    
    
    