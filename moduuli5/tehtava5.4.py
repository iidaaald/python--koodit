#Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan
# (käytä for-toistorakennetta nimien kysymiseen) ja tallentaa ne listarakenteeseen.
# Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa
# järjestyksessä kuin ne syötettiin. käytä for-toistorakennetta nimien kysymiseen
# ja for/in toistorakennetta niiden läpikäymiseen.

lista = []

i = 1
kaupunki = input("Anna kaupungin nimi: ")
while i < 5:
    lista.append(kaupunki)
    kaupunki = input ("Anna kaupungin nimi: ")
    i += 1
for kaupunki in range(1,6):
    print(kaupunki)