#Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
# Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan. Käytä for-toistorakennetta.

import random
arvot = []
kuutioiden_lukumaara = int(input("Arpakuutioiden lukumäärä: "))
while kuutioiden_lukumaara > 0:
    rando = random.randint(1,6)
    arvot.append(rando)
    kuutioiden_lukumaara = kuutioiden_lukumaara - 1

print (sum(arvot))
