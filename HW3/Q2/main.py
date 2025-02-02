"""
Q2
Lylah Majernik
HW3
"""
import pandas as pd

scores = []

loop = True

print("Hello, what would you like to do?")



while loop == True:
    menuSel = int(input("Choose an option:\n 1. Add Score\n 2. Check Scores\n 3. Exit \n"))
    if menuSel == 1:
        username = str(input("Enter the username of the player: \n"))
        score = int(input("Please type the score you would like to add:\n"))
        scores.append([username, score])
        print("Your score was added.")
        loop == True
    elif menuSel == 2:
        menuSel2 = int(input("What would you like to do?\n 1. View all scores\n 2. Search score by username\n"))
        if menuSel2 == 1:
            print("Here is your list of scores:\n")
            df = pd.DataFrame(scores, columns =['Names', 'Score'])
            print(df)
            loop == True
        elif menuSel2 == 2:
            df = pd.DataFrame(scores, columns =['Names', 'Score'])
            search = str(input("Enter the name of the user whose score you would like to search:\n"))
            found = df[df.Names.isin([search])]
            print(found)
    elif menuSel == 3:
        confirm = str(input("Press Y to confirm your exit. \nPress N to return to main menu. \n"))
        confirm.lower()
        if confirm == "y":
            save = scores
            loop == False
            print("Goodbye")
            break
        elif confirm == "n":
            loop == True
    else:
        print("Invalid input")
        loop == True
            
        