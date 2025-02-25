'''HW5 Q2 Majernik'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



df = pd.read_csv('../data/pokemon.csv')

loop = True
team = []

while loop == True:
    menu = int(input('What would you like to do?\n\t1. Add pokemon\n\t2. Generate random team\n\t3. Delete Pokemon\n\t4. Exit\n'))
    if menu == 1:
        if len(team) < 6:
            poke = str(input('Name the pokemon you would like to add\n')).lower()
            if poke not in df['identifier'].values:
                print("This Pokemon does not exist")
            else:
                team.append(poke)
                print('Your Team:')
                n = 0
                for i in team:
                    n += 1
                    print(n, i)
                teamdf = df[df['identifier'].isin(team)]
        if len(team) == 6:
            print('Maximum team of 6 allowed. Please delete pokemon to continue')
            
    elif menu == 2:
        randomTeam = df.sample(6)['identifier']
        team = []
        for i in randomTeam:
            team.append(i)
        print('Your Team:')
        n = 0
        for i in team:
            n += 1
            print(n, i)
        teamdf = df[df['identifier'].isin(team)]
    elif menu == 3:
        if len(team) == 0:
            print("your team is empty")
            loop = True
        else:
            print('Your Team:')
            n = 0
            for i in team:
                n += 1
                print(n, i)
            bye = str(input('Name the pokemon you would like to delete\n')).lower()
            if bye not in team:
                print("This Pokemon isn't on your team")
                loop == True
            else:
                print(f"deleting: {bye}")
                confirm = int(input("press 1 to confirm. press 2 to escape.\n"))
                if confirm == 1:
                    teamdf = df[df['identifier'] != bye]
                    team.remove(bye)
                print('Your Team:')
                n = 0
                for i in team:
                    n += 1
                    print(n, i)
                    
    elif menu == 4:
        print('goodbye')
        b = sns.barplot(data=teamdf, x='identifier',y='base_experience')
        b.set_xticklabels(b.get_xticklabels(),rotation=30) 
        plt.xlabel('Name')
        plt.ylabel('Base XP')
        plt.title('Comparing Base XP of Poke Team')
        plt.show()
        break
    else:
        print('invalid input, please try again')
        loop = True
       