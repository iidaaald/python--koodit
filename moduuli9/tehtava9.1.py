""" Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus,
tämänhetkinen nopeus ja kuljettu matka. Kirjoita luokkaan alustaja, joka asettaa
ominaisuuksista kaksi ensin mainittua parametreina saatuihin arvoihin. Uuden auton nopeus
ja kuljetut matka on asetettava automaattisesti nollaksi. Kirjoita pääohjelma,
jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h).
 Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.
"""
class Auto:
    def __init__(self, rekisteri, huippu):
        self.rekisteri = rekisteri
        self.huippu = huippu
        self.nopeus_nyt = 0
        self.kuljettu_matka = 0

auto1 = Auto("ABC-123", "142")
print(f"rekisteritunnus:{auto1.rekisteri}, huippunopeus:{auto1.huippu}km/h,tämänhetkinen nopeus: {auto1.nopeus_nyt}km/h,matkaa kuljettu: {auto1.kuljettu_matka}km")













