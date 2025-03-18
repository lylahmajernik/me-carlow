""" Majernik Q5 
-user enters pokemon

l = poke 1
r = poke 2
top = height, weight, base xp
bottom = exp over levels 1-100
center = winner: avg xp over 1-100 + strength
center= just the name
"""


import pandas as pd
import numpy as np
import seaborn as sbn
import matplotlib.pyplot as plt


ty = pd.read_csv("../data/types.csv")
t2 = pd.read_csv("../data/pokemon_types.csv")
s = pd.read_csv("../data/pokemon_species.csv")
g = pd.read_csv("../data/generations.csv")
p = pd.read_csv("../data/pokemon.csv")
e = pd.read_csv("../data/experience.csv")

df = ty.merge(t2, how="left", left_on="id", right_on="type_id", suffixes=("_type","_poke"))
df = df.merge(s, how='left',left_on='pokemon_id',right_on='id', suffixes=("","_species"))
df = df.merge(g, how='left', left_on='generation_id_species',right_on='id', suffixes=("","_gen"))
df = df.merge(p, how='left',left_on='id_species', right_on='id', suffixes=("","_poke"))
df = df.merge(e, how ='left',left_on='growth_rate_id', right_on='growth_rate_id', suffixes=("","_exp"))

del ty, t2, s, g, p, e


df = df.rename(columns ={'identifier_species':'poke_identifier','id_species':'poke_id','identifier':'type_identifier','id_gen':'id_gen','identifier_gen':'generation'})
df = df[['poke_identifier','poke_id','type_id','type_identifier','id_gen','generation','height','weight','base_experience','level','experience','growth_rate_id']]
df = df.assign(strength = lambda x: ( (x['height']*5) + (x['weight']*2) + x['experience']))

while True:
    search1 = str(input("Enter the 1st Pokemon you would like to search...\n")).lower()
    if search1 not in df['poke_identifier'].values:
          print("\nI don't know that Pokemon...\n\n")
          continue
    search2 = str(input("Enter the 2nd Pokemon you would like to search...\n")).lower()
    if search2 not in df['poke_identifier'].values:
          print("\nI don't know that Pokemon...\n\n")
          continue


    fig, axs = plt.subplots(3, 3,figsize=(12, 12))
    axs[0, 1].axis('off')
    axs[1, 0].axis('off')
    axs[1, 2].axis('off')
    axs[2, 1].axis('off')
        ##################
    #Poke 1 height, weight, base xp
    poke1 = df[df['poke_identifier'] == search1][['poke_identifier', 'height', 'weight', 'base_experience']].drop_duplicates()
    poke1.plot(kind='bar', x='poke_identifier', y=['height', 'weight', 'base_experience'], color=['red','orange','gold'], ax=axs[0, 0])
    axs[0, 0].set_ylabel('Value')
    axs[0, 0].set_xlabel(f'{search1.title()}')
    axs[0, 0].set_title(f'{search1.title()}: Height, Weight, & Base XP')
    axs[0, 0].legend(loc='upper left')

    axs[0, 0].tick_params(axis='x', which='both', bottom=False, labelbottom=False)
       
    
     
        ###################
    # #Poke 2 height, weight, base xp
    poke2 = df[df['poke_identifier'] == search2][['poke_identifier', 'height', 'weight', 'base_experience']].drop_duplicates()
    poke2.plot(kind='bar', x='poke_identifier', y=['height', 'weight', 'base_experience'], color=['yellowgreen','dodgerblue','rebeccapurple'], ax=axs[0, 2])
    axs[0, 2].set_ylabel('Value')
    axs[0, 2].set_xlabel(f'{search2.title()}')
    axs[0, 2].set_title(f'{search2.title()}: Height, Weight, & Base XP')
    axs[0, 2].legend(loc='upper left')
    
    
    axs[0, 2].tick_params(axis='x', which='both', bottom=False, labelbottom=False)
    plt.tight_layout()
        ###################
    
    
        
    #     ###################
    #Poke 1 xp level 1 - 100
    df1 = df[['poke_identifier', 'level', 'experience']]
    df1 = df1[df1['poke_identifier'] == search1].groupby('level')['experience'].mean().round(0).reset_index(name='avg_xp')
    
    df1['level'] = df1['level'].astype(int)
    df1.plot(kind='line', x='level', y='avg_xp', color=['red'], ax=axs[2, 0])
    axs[2, 0].set_ylabel('Experience')
    axs[2, 0].set_xlabel('Level')
    axs[2, 0].set_title(f'Strength Statistics of {search1.title()} by Level')
    axs[2, 0].legend(['XP'], loc='upper left')
    
    
       
    
        
    #     ################
    # #poke 2 xp lvl 1 - 100
    #     plt.subplot(3,3,9)
    df2 = df[['poke_identifier', 'level', 'experience']]
    df2 = df2[df2['poke_identifier'] == search1].groupby('level')['experience'].mean().round(0).reset_index(name='avg_xp')
    
    df2['level'] = df2['level'].astype(int)
    df2.plot(kind='line', x='level', y='avg_xp', color=['dodgerblue'], ax=axs[2, 2])
    axs[2, 2].set_ylabel('Experience')
    axs[2, 2].set_xlabel('Level')
    axs[2, 2].set_title(f'Strength Statistics of {search2.title()} by Level')
    axs[2, 2].legend(['XP'], loc='upper left')
    
    
    axs[0, 2].legend(loc='upper left')





    pokestat1 = df[df['poke_identifier'] == search1][['experience', 'strength']].mean().sum()
    pokestat2 = df[df['poke_identifier'] == search2][['experience', 'strength']].mean().sum()
    if pokestat1 > pokestat2:
        axs[1,1].text(0.25,0.25,f'Winner:\n{search1.title()}',fontsize=28, color='red')
        axs[1,1].tick_params(axis='x', which='both', bottom=False, labelbottom=False)
        axs[1, 1].tick_params(axis='y', which='both', left=False, labelleft=False)
    elif pokestat2 > pokestat1:
        axs[1,1].text(0.25,0.25,f'Winner:\n{search2.title()}',fontsize=28, color='dodgerblue')
        axs[1,1].tick_params(axis='x', which='both', bottom=False, labelbottom=False)
        axs[1, 1].tick_params(axis='y', which='both', left=False, labelleft=False)
    elif pokestat1 == pokestat2:
        axs[1,1].text(0.25,0.25,'Winner:\n A tie!', fontsize=28,color='yellowgreen')
        axs[1,1].tick_params(axis='x', which='both', bottom=False, labelbottom=False)
        axs[1, 1].tick_params(axis='y', which='both', left=False, labelleft=False)
    else:
        axs[1,1].text(0.25,0.25,'Something went wrong',fontsize=28)
        axs[1,1].tick_params(axis='x', which='both', bottom=False, labelbottom=False)
        axs[1, 1].tick_params(axis='y', which='both', left=False, labelleft=False)

    break    
    
    
    
    


