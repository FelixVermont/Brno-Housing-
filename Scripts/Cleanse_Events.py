import pandas as pd

ev = pd.read_csv('Entertainment\Events.csv')
ev = ev[['objectid','X','Y','name','place_address']]

print(ev)

ev.to_csv('Entertainment\Clean_Events.csv', index=False)