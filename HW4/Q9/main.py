'''
q9
'''
#Here is the original code I had before your email. Keeping just to keep...
import pandas as pd

pokemon = pd.read_csv("../Data/pokemon.csv")

location_areas = pd.read_csv("../Data/location_areas.csv") 

encounters = pd.read_csv("../Data/encounters.csv")

locations = pd.read_csv("../Data/locations.csv")

ab = encounters.merge(pokemon, how='left',left_on="pokemon_id",right_on="id", suffixes =("enc","poke"))
abc = ab.merge(location_areas, how='left',left_on="location_area_id",right_on="id", suffixes =("poke","loca"))
df = abc.merge(locations, how='left',left_on="location_area_id",right_on="id", suffixes =("loca","loc"))

#so this was my original code
#Shows you locations & how many poke found in each
dflylah = df.groupby("identifier")["pokemon_id"].count().sort_values(ascending=False).head(5)


#this is what I gathered from your email. It also worked fine but the actual output felt more confusing to me
#I need to turn this in tho so here is both & make of this what you will, my actual locations are the same either way.
dfprof = df.groupby('location_area_id')["location_area_id"].count().sort_values(ascending=False).head(5).keys()

dfprof = df[df['location_area_id'].isin(dfprof)]
dfprof = dfprof['identifier'].drop_duplicates()


dflylah.to_csv('q9.out')