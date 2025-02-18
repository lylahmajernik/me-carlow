'''q10'''
import pandas as pd

pokemon = pd.read_csv("../Data/pokemon.csv")

location_areas = pd.read_csv("../Data/location_areas.csv") 

encounters = pd.read_csv("../Data/encounters.csv")

locations = pd.read_csv("../Data/locations.csv")

ab = encounters.merge(pokemon, how='left',left_on="pokemon_id",right_on="id", suffixes =("enc","poke"))
abc = ab.merge(location_areas, how='left',left_on="location_area_id",right_on="id", suffixes =("poke","loca"))
df = abc.merge(locations, how='left',left_on="location_area_id",right_on="id", suffixes =("loca","loc"))


dfmost = df.groupby("identifierpoke")["location_id"].count().sort_values(ascending=False).head(5).to_frame()
dfleast = df.groupby("identifierpoke")["location_id"].count().sort_values(ascending=True).head(5).to_frame()
dftop10 = pd.concat([dfleast,dfmost])
#dftop10 = dftop10.rename(columns={'location_id': 'locations_found'}, inplace=True).sort_values(by='locations_found',ascending=True)
maxx = dftop10[dftop10['location_id'] == dftop10['location_id'].max()]
minn = dftop10[dftop10['location_id'] == dftop10['location_id'].min()]

dftop = pd.concat([maxx, minn])

dftop.to_csv('q10.out')

#Did I repeat some things? yes. Most efficient code? no. 