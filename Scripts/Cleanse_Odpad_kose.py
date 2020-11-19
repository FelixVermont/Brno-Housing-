import pandas as pd

kose = pd.read_csv('Environment\odpad_kose.csv')
kose = kose[['MČ','Ulice','LAT','LNG','Typ']]

kose.to_csv('Environment\Clean_odpad_kose.csv')
