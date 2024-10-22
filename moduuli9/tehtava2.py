"""
Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan nopeuden
 muutoksen (km/h). Jos nopeuden muutos on negatiivinen, auto hidastaa.
 Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa. Auton nopeus ei saa
 kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi.
 Jatka pääohjelmaa siten, että auton nopeutta nostetaan
  ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h.
  Tulosta tämän jälkeen auton nopeus. Tee sitten hätäjarrutus
  määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus. Kuljettua matkaa ei tarvitse
  vielä päivittää.
"""

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

auto1 = Auto("ABC-123", "142")
auto1.kiihdytä(30)
auto1.kiihdytä(70)
auto1.kiihdytä(50)
print(auto1.nopeus)
#hätäjarru
auto1.kiihdytä(-200)
print(auto1.nopeus)

print(f"rekisteritunnus:{auto1.rekisteri}, huippunopeus:{auto1.huippu}km/h,tämänhetkinen nopeus: {auto1.nopeus}km/h,matkaa kuljettu: {auto1.kuljettu_matka}km")



