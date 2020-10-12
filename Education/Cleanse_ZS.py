import pandas as pd

zs = pd.read_csv(r'Education\skolyzs.csv')
#tady to nactu

zs = zs[['Nazev', 'Ulice/PSC']]
# tady dam co chci

zs.columns = (['Nazev', 'Adresa'])
#prejmenovani


print(zs)

zs.to_csv(r'Education\skolyzs.csv', index = False)