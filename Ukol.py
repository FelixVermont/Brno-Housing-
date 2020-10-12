import json

studenti = []
# Part 1
with open('studenti.txt', encoding='utf-8') as subor:
    for line in subor.readlines():
        line = line.rstrip()
        studenti += [line.split('\t')]
        
studenti = studenti[1:]

# Part 2
for radek in studenti:
    cislo = radek[2]
    rok = 1900 + int(cislo[:2])
    vek = 2020 - rok
    radek += [vek]

# Part 3
for radek in studenti:
    cislo = radek[2]
    cislo = int(cislo[2])
    if cislo < 5:
        radek += ['m']
    else:
        radek += ['f']

# Part 4
for radek in studenti:
    first = radek[0]
    second = radek[1]
    name = first[:5] + second[:3] + '@hybrid.edu'
    radek += [name.lower()]

# Part 5
vystup = []
for radek in studenti:
    slovnik = {
        'jmeno' : radek[0],
        'prijmeni' : radek[1],
        'rodne_cislo' : radek[2],
        'vek' : radek[3],
        'pohlavi' : radek[4],
        'email' : radek[5],  
    }
    vystup.append(slovnik)
print(vystup)

vysledek = open('vystup.json', 'w')
json.dump(vystup, vysledek)
vysledek.close()
