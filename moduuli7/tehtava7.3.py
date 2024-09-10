#Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi.
# Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman, hakea
# jo syötetyn lentoaseman tiedot vai lopettaa. Jos käyttäjä valitsee uuden
# lentoaseman syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen.
# Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen.
# Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy. Käyttäjä saa valita uuden toiminnon
# miten monta kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa.
# (ICAO-koodi on lentoaseman yksilöivä tunniste. Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK.
# Löydät koodeja helposti selaimen avulla.)
sanakirja ={}
while True:
    komento = input("haluatko syöttää uuden lentoaseman (uusi lentoasema)"
                    ", hakea jo syötetyn lentoaseman tiedot (hakea) "
                    "vai lopettaa? (lopeta): ")
    if komento == "uusi lentoasema":
        icao = input("mikä on lentoaseman ICAO- koodi: ")
        nimi = input("mikä on lentoaseman nimi: ")
        sanakirja.update({icao: nimi})
    if komento == "hakea":
        nimi = input("Mikä on ICAO- koodi: ")
        if nimi in sanakirja:
            print(sanakirja[nimi])
    if komento == "lopeta":
        break