import pandas as pd
import numpy as np



df = pd.read_csv("data/poke.csv")

names = df['identifier']
idNum = df['id']
    
userPoke = str(input("Search Pokemon: \n")).lower()

if userPoke in df.identifier.values:  
    pokeIndex = df[df['identifier'] == userPoke].index[0]
    #^^I need you to know this was ChatGPT-ified....which is fine because i mostly understand
    #except I don't know why I need to put index[0] instead of just .index... 
    print("Pokemon: ",userPoke.capitalize(),"\nIndex: ", pokeIndex)
    file = open('q6.out', 'w')
    file.write("Pokemon: " + userPoke.capitalize() + "\nIndex: " + str(pokeIndex))
    file.close()
else:
    print("This is not a Pokemon...yet")