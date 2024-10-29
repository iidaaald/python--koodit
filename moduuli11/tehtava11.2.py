'''
Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto.
Sähköautolla on ominaisuutena akkukapasiteetti kilowattitunteina. Polttomoottoriauton
ominaisuutena on bensatankin koko litroina. Kirjoita aliluokille alustajat. Esimerkiksi
sähköauton alustaja saa parametreinaan rekisteritunnuksen, huippunopeuden ja akkukapasiteetin.
Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi sekä asettaa oman kapasiteettinsa.
Kirjoita pääohjelma, jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh) ja
yhden polttomoottoriauton (ACD-123, 165 km/h, 32.3 l). Aseta kummallekin autolle haluamasi nopeus,
 käske autoja ajamaan kolmen tunnin verran ja tulosta autojen matkamittarilukemat
'''

import random

class Auto:
    def __init__(self, rekisteri, huippu):
        self.rekisteri = rekisteri
        self.huippu = huippu
        self.nopeus = 30
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

class Sähköauto (Auto):
    def __init__(self, rekisteri, huippu, kapasiteetti):
        super().__init__(rekisteri, huippu)
        self.kapasiteetti = kapasiteetti

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteri, huippu, tankki_koko):
        super().__init__(rekisteri, huippu)
        self.tankki_koko = tankki_koko

#Pääohjelma
sähkö_auto = Sähköauto("ABC-15", 180, 52.5)
bensa_auto = Polttomoottoriauto("ACD-123", 165, 32.3)
sähkö_auto.kulje(2)
bensa_auto.kulje(3)
print(f"Sähköauton kulkema matka:{sähkö_auto.kuljettu_matka} km")
print(f"Polttomoottoriauton kulkema matka:{bensa_auto.kuljettu_matka} km")

