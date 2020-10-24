import pandas as pd


zsams = pd.read_csv(r'Education\zsAMs.csv')
#tady to nactu

zsams = zsams[['Nazev', 'Ulice/PSC']]
# tady dam co chci

zsams.columns = ['Nazev', 'Adresa']
#prejmenovani

print(zsams)

zsams.to_csv(r'Education\zakladniamaterskekoly.csv', index = False)