import pandas as pd

zs = pd.read_csv('Doprava\MHD_zastavky.csv')

zs = zs[['X','Y','stop_name','zone_id']]

zs1 = zs[zs.zone_id == 100]
zs2 = zs[zs.zone_id == 101]

zs_new = pd.concat([zs1,zs2], axis = 1)
zs_new.to_csv('Doprava\Clean_MHD_zastavky.csv', index = False)

print(zs_new)