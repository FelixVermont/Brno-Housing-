#!/usr/bin/env python3

import pandas as pd
import numpy as np

realset = pd.read_csv('Reality/bezrealitky-brno-prodej.csv')
realset = realset[['city','city_district','price','type','area','building_type','penb','equipment','floor','balcony','terace','lift','garage', 'coordinates']]

realset[['lat','lon']] = realset['coordinates'].str.split(',',1,expand=True)

realset = realset[['city','city_district','price','type','area','building_type','penb','equipment','floor','balcony','terace','lift','garage', 'lat','lon']]

realset = realset[realset['city']=='Brno']
purchase = 'purchase'
realset['demand'] = purchase

#amenities
realset['cellar'] = np.random.randint(0,2, realset.shape[0])

#car
realset['parking'] = np.random.randint(0,2, realset.shape[0])

#state
realset['state'] = np.random.randint(0,3, realset.shape[0])

realset.to_csv(r'Reality/Full_Realset_purchase.csv', index = False)