"""
Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän.
 Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa
 tuntimäärässä edennyt. Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km.
  Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.

"""

class Auto:
    def __init__(self, rekisteri, huippu):
        self.rekisteri = rekisteri
        self.huippu = int(huippu)
        self.nopeus = 0
        self.kuljettu_matka = 2000

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

auto1 = Auto("ABC-123", "142")
auto1.kiihdytä(60)
auto1.kulje(1.5)
#hätäjarru
auto1.kiihdytä(-200)
print(auto1.nopeus)

print(f"rekisteritunnus:{auto1.rekisteri}, huippunopeus:{auto1.huippu}km/h,tämänhetkinen nopeus: {auto1.nopeus}km/h,matkaa kuljettu: {auto1.kuljettu_matka}km")



