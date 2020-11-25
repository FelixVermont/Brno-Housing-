import pandas as pd
import os

fm = pd.read_csv(os.path.join('Práce','Firms.csv'))

fm = fm[['X', 'Y', 'název', 'počet_zaměstnanců', 'odvětví', 'address']]

print(fm)

fm.to_csv(r'Práce\Clean_Firms.csv', index = False)
