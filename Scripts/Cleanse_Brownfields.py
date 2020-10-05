import pandas as pd

bf = pd.read_csv('Special graphs\Brownfields.csv')

bf = bf[['nazev','adresa','katastralni_uzemi','puvodni_ucel','kontaminace_lokality','skladky','dostupnost_mhd','ver_osv','lokalita_ss','lokalita_r','exekuce','shape_Length','shape_Area']]

bf.columns = ['nazev','adresa','katastralni_uzemi','puvodni_ucel','kontaminace','skladky','dostupnost_mhd','osvetleni','soudni_spor','restituce','exekuce','shape_length','shape_area']

print(bf)

bf.to_csv(r'Special graphs\Clean_Brownfields.csv', index = False)