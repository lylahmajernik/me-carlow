'''HW5 Q9 Majernik'''

import numpy as np
import pandas as pd

#This question was quite a doozy
#This is not perfect but I have to give in. 


#set up one big clean df

p = pd.read_csv('../data/pokemon.csv')
l = pd.read_csv('../data/locations.csv')
r = pd.read_csv('../data/regions.csv')
e = pd.read_csv('../data/encounters.csv')

df = p.merge(e, how ='left',left_on='id',right_on='pokemon_id',suffixes=('_poke','_enc'))
df = df.merge(l, how ='left',left_on='location_area_id',right_on='id',suffixes=('','_loc'))
df = df.merge(r, how ='left',left_on='region_id',right_on='id',suffixes=('','_reg'))

del p, l, r, e

df = df[['id_poke','identifier','base_experience','identifier_loc','identifier_reg','encounter_slot_id']]


##############################################################################################################



#Setting up the dungeon
dungeon = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

#giving dungeon random start and exit
start = np.random.randint(1,16) #Dr. Mochan suggested randint
exitt = np.random.randint(1,16)

#make sure start and exit are not the same
while exitt == start:
    exitt = np.random.randint(1,16)

#set player to start at start    
position = start


#idk if any of these are even needed
game = True
build = True
play = True
team = []
enemies = []
###################################################################################################################

#Get a name and a region
#make sure region or location exists in our data frame
#too many while loops already so if it doesnt they get a random one

master = str(input("What is your name?\n\t"))
where = str(input("First pick the region or location your dungeon is in.\n\t"))

#checking df for validation of location
if where not in df['identifier_reg'].values and where not in df['identifier_loc'].values:
    print("That place doesn't exist. A random location is being assigned...")
    where = df['identifier_reg'].dropna().sample(1).iloc[0]  
    print(f"Oh, we're in {where}...")
else:
    if where in df['identifier_reg'].values:
        print(f"Oh, we're in {where}...")
    else:
        print(f"Oh, we're in {where}.")
        
    
#setting up random enemy selection, have to make 2 conditions for region or location.
#I don't think this works how I want it to but I do not have time ti change it.
#half the locs register as unknown and then you get a random region
if where in df['identifier_reg'].values:
    enemies = df[df['identifier_reg'] == where].sample(14)['identifier'].tolist()
elif where in df['identifier_loc'].values:
    enemies = df[df['identifier_loc'] == where].sample(14)['identifier'].tolist()
else:
    enemies = df[df['identifier_reg'] == where].sample(14)['identifier'].tolist()  
    
#I wanted to have this info as a list of just names and a df. idk why.
#making a dataframe of these enemies so I can acess their base xp  later and not just their names
enemydf = df[df['identifier'].isin(enemies)]

###################################################################################################################

##quite honestly have no idea here and used chat gpt. just keeping it real. 
#my prompt was: if I have ranodm enemies and an array of random cells how do i assign those enemies to the cells

dungeon_positions = [cell for row in dungeon for cell in row if cell not in [start, exitt]]

#but, then we're back on track and making a dict. 
enemy_positions = dict(zip(dungeon_positions, enemies))
            
         
#Now the actual problem. This is modiefied from my previous hw.            
    
print("~~~~~~~~~~~~~~~~~~~~~~~~")
print("Now it's time to build your team")

###Team building    
while build != 5:
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
            print('Maximum team of 6 allowed. Please delete pokemon to continue, or press 4 if you are ready to fight.')
            
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
        print('Time to fight!')
        build == 5
        break
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
        break
    
    else:
        print('invalid input, please try again')
        
###################################################################################################################################################################      
###playing the game


##So tbh I did question 10 from the hw a while ago first. Once I got that, I modified it to be 4*4.
##I did this with some help from Dr. Mochan
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("You're in a dungeon...that's not good!")
print("Use WASD to move around.\nAt any time press 4 to exit\n")
i = 0
while position != exitt:  
    move = str(input("Move: ")).lower()

    if move in ['w', 'a', 's', 'd']:
        if move == 'w':  
            if position not in [1, 2, 3, 4]:
                position -= 4
                i += 1
                print("Moving up...")
            else:
                print("Can't move up. Must be a wall.")
                i += 1

        elif move == 'a':  
            if position not in [1, 5, 9, 13]:
                position -= 1
                i += 1
                print("Moving left...")
            else:
                print("Can't move left. Must be a wall.")
                i += 1

        elif move == 's':  
            if position not in [12, 13, 14, 15]:
                position += 4
                i += 1
                print("Moving down...")
            else:
                print("Can't move down. Must be a wall.")
                i += 1

        elif move == 'd':  
            if position not in [4, 8, 12, 16]:
                position += 1
                i += 1
                print("Moving right...")
            else:
                print("Can't move right. Must be a wall.")
                i += 1
#Dobby loves that I made the name variable master
    elif move == '4':  
        print(f"You're a quitter, {master}. You lose.")
        print(f'Number of moves before failure: {i}')
        file = open('status.out','w')
        file.write("failure")
        file.close()
        break

    else:
        print("Invalid input. Use WASD to move.")
        
    if position in enemy_positions:
            enemy = enemy_positions[position]
            print(f"You've encountered {enemy}!")

            if len(team) == 0:
                print("You have no Pokémon left! You lose.")
                break

            fighter = team[0]

            
            fighter_stats = df[df['identifier'] == fighter]['base_experience'].values[0]
            enemy_stats = df[df['identifier'] == enemy]['base_experience'].values[0]

            
            if fighter_stats >= enemy_stats:
                print(f"{master} plays {fighter}")
                print('\n\n~~~~~~')
                print(f"{fighter} wins. {enemy} is defeated\n\n~~~~~~")
                del enemy_positions[position]
            else:
                print(f"{master} plays {fighter}")
                print('\n\n~~~~~~')
                print(f"{fighter} was defeated by {enemy}!\n\n~~~~~~")
                team.remove(fighter) 
                teamdf = df[df['identifier'].isin(team)]

            if len(team) == 0:
                print(f"womp womp. All your Pokémon have been defeated. Game over! Try again, {master}!")
                file = open('status.out','w')
                file.write("failure")
                file.close()
                break

    elif move == '4':  
        print(f" You're a quitter, {master}... You lose.")
        file = open('status.out','w')
        file.write("failure")
        file.close()
        break


if position == exitt:
    print(f"You've escaped, {master}!")
    print(f'Number of moves: {i}')
    length = str(len(team))
    file = open('status.out','w')
    file.write("success\n")
    file.write("remaining poke: " + length)
    file.close()

    success = True