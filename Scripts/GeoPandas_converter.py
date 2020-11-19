import pandas as pd    
from geopy.geocoders import Nominatim

df = pd.read_csv('C:/Users/adamc/Desktop/data/Ikikata/Ikikata_Data/Entertainment/divadlaDone.csv')
locator = Nominatim(user_agent='myGeocoder')

df['lat'] = 0 
df['lon'] = 0

for index, row in df.iterrows():
    try:
        location = locator.geocode(row['Adresa'])
        df.loc[index,'lat'] = location.latitude 
        df.loc[index,'lon'] = location.longitude
        #print(location.latitude)
        #print(location.longitude)
    except:
        print('Zero value')

df.to_csv('C:/Users/adamc/Desktop/data/Ikikata/Ikikata_Data/Entertainment/divadlaA_geopd.csv')

        
