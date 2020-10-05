import pandas as pd

fm = pd.read_csv('Práce\Firms.csv')

fm = fm[['X', 'Y', 'název', 'počet_zaměstnanců', 'odvětví', 'address', 'latitude', 'longitude']]

print(fm)

fm.to_csv(r'Práce\Clean_Firms.csv', index = False)
