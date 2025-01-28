import pandas as pd
import numpy as np



df = pd.read_csv("data/poke.csv")

names = df['identifier']
idNum = df['id']

pokeTeam = []

pokePlyr = str(input("Enter a Pokemon to start building your team.\n")).lower()


while pokePlyr != "exit":
    if pokePlyr in df.identifier.values:    
            if len(pokeTeam) < 6:  
                pokePlyr = pokePlyr.capitalize() 
                pokeTeam.append(pokePlyr)  
                if len(pokeTeam) == 6:
                    print("Your team is full.")
                    print(pokeTeam)
                    pokePlyr = str(input("New team members will remove your first player. Or, type 'exit' to stop: \n").lower())
                    if pokePlyr != 'exit':
                        pokeTeam.pop(0) 
                        continue
                else:
                    pokePlyr = str(input("List another team member or type 'exit' to stop: \n").lower())  

                     
            
            if pokePlyr == "exit":
                file = open('q7.out', 'w')
                file.write("Your Team: \n")
                for i in pokeTeam:
                    file.write(i +"\n")
                print("Here is your team:\n", pokeTeam)
    else:
        print("Invalid input.")
        pokePlyr = str(input("I meant to say..."))
        
    
file.close()