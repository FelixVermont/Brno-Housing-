#!/usr/bin/env python3

import pandas as pd

final_cols = ["nazev", "kategorie", "adresa", "lat", "lon"]

obchody = pd.read_csv('Obchody/obchodyGeopd.csv')
obchody.columns = ["nazev", "adresa", "lat", "lon"]
obchody["kategorie"] = "obchod"

cukrarny = pd.read_csv('Entertainment/cukrarnygeopd.csv')
cukrarny.columns = ["id", "nazev", "adresa", "kategorie", "lat", "lon"]
cukrarny["kategorie"] = "kavarna"

divadla = pd.read_csv('Entertainment/divadla_geopd.csv')
divadla.columns = ["id", "nazev", "adresa", "lat", "lon"]
divadla["kategorie"] = "divadlo"

kina = pd.read_csv('Entertainment/kina_geopd.csv')
kina.columns = ["id", "nazev", "adresa", "lat", "lon"]
kina["kategorie"] = "kino"

pivnice = pd.read_csv('Entertainment/pivnice_geopd.csv')
pivnice.columns = ["id", "nazev", "adresa", "kategorie", "lat", "lon"]
pivnice["kategorie"] = "vinarna"

restaurace = pd.read_csv('Entertainment/Restaurace_geopd.csv')
restaurace.columns = ["id", "nazev", "adresa",
                      "kategorie", "lat", "lon"]

rod_restaurace = pd.read_csv('Entertainment/rodinneRestaurace_geopd.csv')
rod_restaurace.columns = ["id", "nazev",
                          "adresa", "kategorie",
                          "podkategorie", "lat", "lon"]
rod_restaurace["kategorie"] = "rod. restaurace"

sport = pd.read_csv('Entertainment/sport_geopd.csv')
sport.columns = ["id", "nazev", "adresa", "lat", "lon"]
sport["kategorie"] = "divadlo"

vinarny = pd.read_csv('Entertainment/vinarny_geopd.csv')
vinarny.columns = ["id", "nazev", "adresa", "kategorie", "lat", "lon"]

skola_mater_priv = pd.read_csv('Schools/materske_privateGeopd.txt')
skola_mater_priv.columns = ["nazev", "adresa", "psc", "lat", "lon"]
skola_mater_priv["kategorie"] = "skolka"

skola_mater = pd.read_csv('Schools/materskeGeopd.txt')
skola_mater.columns = ["id", "nazev", "adresa", "psc", "lat", "lon"]
skola_mater["kategorie"] = "skolka"

skola_stredni = pd.read_csv('Schools/stredniGeopd.txt')
skola_stredni.columns = ["id", "nazev", "adresa", "lat", "lon"]
skola_stredni["kategorie"] = "stred. skola"

skola_zakl = pd.read_csv('Schools/zakladniGeopd.txt')
skola_zakl.columns = ["id", "nazev", "adresa", "psc", "lat", "lon"]
skola_zakl["kategorie"] = "zakl. skola"

skola_zakl_mater = pd.read_csv('Schools/zakladni_materskeGeopd.txt')
skola_zakl_mater.columns = ["id", "nazev", "adresa", "psc", "lat", "lon"]
skola_zakl_mater["kategorie"] = "skolka"

skola_zakl_mater2 = pd.read_csv('Schools/zakladni_materskeGeopd.txt')
skola_zakl_mater2.columns = ["id", "nazev", "adresa", "psc", "lat", "lon"]
skola_zakl_mater2["kategorie"] = "zakl. skola"

skola_vysoka = pd.read_csv('Práce/vysokeSkoly.txt')
skola_vysoka.columns = ["id", "nazev", "adresa", "lat", "lon"]
skola_vysoka["kategorie"] = "vys. skola"

prace = pd.read_csv('Práce/Clean_Firms.csv')
prace.columns = ["lon", "lat", "nazev", "pocet zam.", "odvetvi", "adresa"]
prace["kategorie"] = "firma"

prac_strediska = pd.read_csv('Práce/pracovniStrediska.txt')
prac_strediska.columns = ["id", "nazev", "lat", "lon"]
prac_strediska["kategorie"] = "prac. stredisko"

parky = pd.read_csv('Environment/parky.txt')
parky.columns = ["id", "nazev", "lat", "lon"]
parky["kategorie"] = "park"

zastavky = pd.read_csv('Doprava/Clean_MHD_zastavky.csv')
zastavky.columns = ["lon", "lat", "nazev", "zona"]
zastavky["kategorie"] = "zastavka"

final_df = pd.concat([obchody, cukrarny, divadla, kina, pivnice,
                      restaurace, rod_restaurace, sport, vinarny,
                      skola_mater_priv, skola_mater, skola_zakl_mater, skola_zakl_mater2,
                      skola_zakl, skola_stredni, skola_vysoka, prace,
                      prac_strediska, parky, zastavky]).reset_index()
final_df = final_df[final_cols]
final_df.to_csv("Reality/complete_set.csv")
