'''
Tehtävä on jatkoa aiemmalle autokilpailutehtävälle. Kirjoita Kilpailu-luokka, jolla on ominaisuuksina kilpailun nimi,
pituus kilometreinä ja osallistuvien autojen lista. Luokassa on alustaja, joka saa parametreinaan nimen, kilometrimäärän
ja autolistan ja asettaa ne ominaisuuksille arvoiksi. Luokassa on seuraavat metodit:

tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut tunnin välein tehtävät toimenpiteet eli
arpoo kunkin auton nopeuden muutoksen ja kutsuu kullekin autolle kulje-metodia.
tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi taulukoksi muotoiltuna.
kilpailu_ohi, joka palauttaa True, jos jokin autoista on maalissa eli se on ajanut vähintään kilpailun
 kokonaiskilometrimäärän. Muussa tapauksessa palautetaan False.
Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä "Suuri romuralli". Luotavalle kilpailulle
annetaan kymmenen auton lista samaan tapaan kuin aiemmassa tehtävässä. Pääohjelma simuloi kilpailun etenemistä
 kutsumalla toistorakenteessa tunti_kuluu-metodia, jonka jälkeen aina tarkistetaan kilpailu_ohi-metodin avulla,
 onko kilpailu ohi. Ajantasainen tilanne tulostetaan tulosta tilanne-metodin avulla kymmenen tunnin välein sekä
 kertaalleen sen jälkeen, kun kilpailu on päättynyt.
'''

import random

class Auto:
    def __init__(self, rekisteri, huippu):
        self.rekisteri = rekisteri
        self.huippu = huippu
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, muutos):
        uusi = self.nopeus + muutos
        if uusi > self.huippu:
            self.nopeus = self.huippu
        elif uusi < 0:
            self.nopeus = 0
        else:
            self.nopeus = uusi

    def kulje(self, tunnit):
        yeah = tunnit * self.nopeus + self.kuljettu_matka
        self.kuljettu_matka = yeah

class Kilpailu:
    def __init__(self, kilpailun_nimi, pituus, autot):
        self.kilpailun_nimi = kilpailun_nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in autot:
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdytä(nopeuden_muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"Kilpailu: {self.kilpailun_nimi}:")
        print(f"{'AUTOT:'} {'NOPEUS (km/h):'} {'KULJETTU MATKA (km):'}")
        for auto in self.autot:
            print(f"{auto.rekisteri} {auto.nopeus} {auto.kuljettu_matka}")
        print("-" *30)

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus:
                return True
            return False

#Pääohjelma
autot = []
for i in range(10):
    autot.append(Auto(f"ABC-{i + 1}", random.randint(100,200)))

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)
tunnit = 0
while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunnit += 1
    if tunnit % 10 == 0:
        kilpailu.tulosta_tilanne()
kilpailu.tulosta_tilanne()
print("Kilpailu on päättynyt!!!")
