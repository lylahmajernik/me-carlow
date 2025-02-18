# -*- coding: utf-8 -*-
import pandas as pd
df = pd.read_csv("../Data/pokemon.csv")

loop = True

while loop == True:
    menu1 = int(input("What would you like to do?\n1.Manage Dataset\n2.Exit\n"))
    if menu1 == 1:
        menu2 = int(input('Would you like to:\n\t1. Add Pokemon\n\t2. Delete Pokemon\n\t3. Update Pokemon\n\t4. Exit\n'))
        if menu2 == 1:
            #I definitley could have made these a little more user-error-resistant with a bunch of while loops and if statements but time...
            newPoke = dict.fromkeys(df.columns)
            newPoke['id'] = int(input('Enter Poke id\n'))
            newPoke['identifier'] = str(input('Enter Poke name\n'))
            newPoke['species_id'] = int(input('Enter Poke species id\n'))
            newPoke['height'] = int(input('Enter Poke height\n'))
            newPoke['weight'] = int(input('Enter Poke weight\n'))
            newPoke['base_experience'] = int(input('Enter Poke base xp\n'))
            newPoke['order'] = int(input('Enter Poke order\n'))
            newPoke['is_default'] = int(input('If the Poke is default, enter 1. If not, enter 0.\n'))
            newdf = pd.DataFrame([newPoke])
            print(f'Here is your new Pokemon {newdf}')
            df = pd.concat([df,newdf]).sort_values(by='id')
        elif menu2 == 2:
            bye = int(input("Enter the id number of the poke you'd like to delete\n"))
            print(f"deleting: {df.loc[df['id'] == bye, 'identifier'].values[0]}")
            confirm = int(input("press 1 to confirm. press 2 to escape."))
            if confirm == 1:
                df = df[df['id'] != bye]
            else:
                continue
        elif menu2 == 3:
            change = int(input("Enter the id number of the poke you'd like to rename\n"))
            print(f"youd like to change: {df.loc[df['id'] == change, 'identifier'].values[0]}")
            newName = str(input("What would you like to change this pokemon's name to?\n"))
            print(f"You are changing {df.loc[df['id'] == change, 'identifier'].values[0]} to {newName}?")
            confirm = int(input("press 1 to confirm. press 2 to escape."))
            if confirm == 1:
                df.loc[df['id'] == change, 'identifier'] = newName            
            else:
                continue
                
        else:
            break
    elif menu1 == 2:
        print("Goodbye")
        break
    else:
        print('Invalid input. Please type 1 to manage dataset, or 2 to exit.\n')
            
df.to_csv('q13.out')