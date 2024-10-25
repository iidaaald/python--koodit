'''
Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan. Talon alustajaparametreina annetaan
alimman ja ylimmän kerroksen numero sekä hissien lukumäärä. Talon luonnin yhteydessä talo luo
tarvittavan määrän hissejä. Hissien lista tallennetaan talon ominaisuutena. Kirjoita taloon metodi
aja_hissiä, joka saa parametreinaan hissin numeron ja kohdekerroksen. Kirjoita pääohjelmaan lauseet
talon luomiseksi ja talon hisseillä ajelemiseksi.
'''

class Hissi:
    def __init__(self,alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def siirry_kerrokseen(self, num):
        if num > self.ylin_kerros:
            print(f"Ylin kerros on {self.ylin_kerros}. hissi ei voi kulkea {num} kerrokseen."
                  f" Mennän rakennuksen ylimpään kerrokseen")
            num = self.ylin_kerros
        elif num < self.alin_kerros:
            print(f"Alin kerros on {self.alin_kerros}. hissi ei voi kulkea {num} kerrokseen."
                  f" Mennän rakennuksen ylimpään kerrokseen.")
            num = self.ylin_kerros

        while self.nykyinen_kerros <num:
            self.kerros_ylös()
        while self.nykyinen_kerros > num:
            self.kerros_alas()
        if self.nykyinen_kerros == num:
            print("Olet saapunut määränpäähääsi!")


    def kerros_ylös(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros = 1 + self.nykyinen_kerros
            print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}")
        else:
            print(f"Hissi on ylimmässä kerroksessa")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros = self.nykyinen_kerros - 1
            print(f"Hissi on kerroksessa {self.nykyinen_kerros}")
        else:
            print(f"Hissi on alimmassa kerroksessa")

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lukumaara):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit = []
        for i in range(hissien_lukumaara):
            uusi =  Hissi(alin_kerros, ylin_kerros)
            self.hissit.append(uusi)

    def aja_hissia(self, hissin_numero, kohde_kerros):
        if hissin_numero < 1 or hissin_numero > len(self.hissit):
            print(f"Virhe: hissiä numero {hissin_numero} ei ole olemassa.")
            return
        self.hissit[hissin_numero -1].siirry_kerrokseen(kohde_kerros)

#Pääohjelma
talo = Talo(0, 10, 3)
talo.aja_hissia(1, 4)
talo.aja_hissia(2, 2)
talo.aja_hissia(3, 8)
talo.aja_hissia(2, 7)
