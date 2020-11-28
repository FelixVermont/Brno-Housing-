#!/usr/bin/env python3

import pandas as pd
import numpy as np

realset = pd.read_csv('Reality/bezrealitky-brno-pronajem.csv')

realset = realset[['city','city_district','price','type','area','building_type','penb','equipment','floor','balcony','terace','lift','garage', 'coordinates']]

realset[['lat','lon']] = realset['coordinates'].str.split(',',1,expand=True)

realset = realset[['city','city_district','price','type','area','building_type','penb','equipment','floor','balcony','terace','lift','garage', 'lat', 'lon']]

realset = realset[realset['city']=='Brno']

rent = 'Rent'
realset['demand'] = rent

# tenants
realset['group'] = np.random.randint(0,2, realset.shape[0])
realset['individual'] = np.random.randint(0,2, realset.shape[0])
realset['family'] = np.random.randint(0,2, realset.shape[0])

#sex
realset['men'] = np.random.randint(0,2, realset.shape[0])
realset['women'] = np.random.randint(0,2, realset.shape[0])

# age
realset['students'] = np.random.randint(0,2, realset.shape[0])
realset['working'] = np.random.randint(0,2, realset.shape[0])
realset['pensioners'] = np.random.randint(0,2, realset.shape[0])

#amenities
realset['cellar'] = np.random.randint(0,2, realset.shape[0])

#car
realset['parking'] = np.random.randint(0,2, realset.shape[0])

#luxury
realset['pets'] = np.random.randint(0,2, realset.shape[0])
realset['smoking'] = np.random.randint(0,2, realset.shape[0])

#state
realset['state'] = np.random.randint(0,3, realset.shape[0])

realset.to_csv(r'Reality/Full_Realset_pronajem.csv', index = False)
