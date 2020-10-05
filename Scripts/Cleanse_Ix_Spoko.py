import pandas as pd

ixs = pd.read_csv('Special graphs\Index_Spokojenosti.csv')

ixs = ixs[['charakter','Shape_Leng','Index_spokojenosti','Ochota_zit_rozhodne_ano','Ochota_zit_spise_ano','Ochota_zit_spise_ne','Ochota_zit_rozhodne_ne','Ochota_zit_nevi','Ochota_zit_pocet_respondentu','SHAPE_Length','SHAPE_Area']]

# oz = ochota zit
ixs.columns = ['charakter','shape_len','ix_spoko','oz_rozhodne_a','oz_spise_a','oz_spise_n','oz_ozhodne_n','oz_nevi','oz_pocet_respondentu','shape_length','shape_area']

print(ixs)

ixs.to_csv(r'Special graphs\Clean_Index_Spokojenosti.csv', index = False)
