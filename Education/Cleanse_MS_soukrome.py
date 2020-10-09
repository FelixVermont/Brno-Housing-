import pandas as pd

mss = pd.read_csv(r'Education\materskeSoukrome.csv')
#tady to nactu

mss = mss[['Nazev', 'Ulice/PSC']]
# tady dam co chci

mss.columns = ['Nazev', 'Adresa']
#prejmenovani

print(mss)

mss.to_csv(r'Education\materskeSoukrome.csv', index = False)