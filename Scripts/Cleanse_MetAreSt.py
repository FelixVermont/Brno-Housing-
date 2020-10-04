# here we import the pandas module names as pd, for ease of use
import pandas as pd

# here we load the csv file into the script
mas = pd.read_csv('Special graphs\Metro_Area_Stats.csv')

# here we pick all of the columns that we deem relevant
mas = mas[['NAZ_OBEC', 'KOD_POU', 'NAZ_LAU1', 'NAROZENI','ZEMRELI','PRISTEHOVALI','VYSTEHOVALI','POCET_OBYV','OBYV_0_14','OBYV_15_64', 'OBYV_65', 'MIRA_NEZAM']]

# here we rename them with better names
mas.columns = ['obec', 'psc', 'okres', 'born','died','moved_in','moved_out','population','ppl_0_14','ppl_15_64', 'ppl_65', 'unemployment_ix']

#here we print the newly edited data for confirmation
print(mas)

# here we save the clean data frame into a new csv file
mas.to_csv(r'Special graphs\Clean_Metro_Area_Stats.csv', index = False)
