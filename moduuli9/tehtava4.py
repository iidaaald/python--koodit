"""
Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi.
Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta.
Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä. Rekisteritunnus luodaan
seuraavasti "ABC-1", "ABC-2" jne. Sitten kilpailu alkaa. Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:

Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä.
Tämä tehdään kutsumalla kiihdytä-metodia.
Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.
Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä. Lopuksi tulostetaan kunkin
auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.
"""
import random

class Auto:
    def __init__(self, rekisteri, huippu):
        self.rekisteri = rekisteri
        self.huippu = int(huippu)
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, muutos):
        uusi = self.nopeus + muutos
        if uusi > self.huippu:
            self.nopeus = self.huippu
        if uusi < 0:
            self.nopeus = 0
        else:
            self.nopeus = uusi

    def kulje(self, tunnit):
        yeah = tunnit * self.nopeus + self.kuljettu_matka
        self.kuljettu_matka = yeah


#Pääohjelma

autot = []
autot.append(Auto("ABC-1", random.randint(100,200)))
autot.append(Auto("ABC-2", random.randint(100,200)))
autot.append(Auto("ABC-3", random.randint(100,200)))
autot.append(Auto("ABC-4", random.randint(100,200)))
autot.append(Auto("ABC-5", random.randint(100,200)))
autot.append(Auto("ABC-6", random.randint(100,200)))
autot.append(Auto("ABC-7", random.randint(100,200)))
autot.append(Auto("ABC-8", random.randint(100,200)))
autot.append(Auto("ABC-9", random.randint(100,200)))
autot.append(Auto("ABC-10", random.randint(100,200)))
while True:
    for auto in autot:
        nopeus = random.randint(-10, 15)
        auto.kiihdytä(nopeus)
        auto.kulje(1)
        if auto.kuljettu_matka >= 10000:
            break
#taulukon luonti



