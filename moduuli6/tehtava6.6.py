#Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä
# sekä pizzan hinnan euroina. Funktio laskee ja palauttaa pizzan yksikköhinnan euroina
# per neliömetri. Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa,
# kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta).
# Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.
import math

def pizza_hinta(cm,e):
    cm2 = math.pi * (float(cm)/2)**2
    m2 = cm2/10000
    yksikköhinta = float(e) / m2
    return yksikköhinta

halkaisija1 = input("Mikä on ensimmäisen pizzan halkaisija senttimetreinä: ")
hinta1 = input("Mikä on ensimmäisen pizzan hinta euroina: ")
halkaisija2 = input("Mikä on toisen pizzan halkaisija senttimetreinä: ")
hinta2 = input("Mikä on toisen pizzan hinta euroina: ")


eka = (pizza_hinta(halkaisija1, hinta1))
toka = (pizza_hinta(halkaisija2,hinta2))
print(f"Ensimmäisen pizzan yksikköhinta:{eka:20.2f} e/m^2")
print(f"Toisen pizzan yksikköhinta:{toka:20.2f} e/m^2")
if eka < toka:
    print("Ensimmäisellä pizzalla on pienempi yksikköhinta.")
if eka > toka:
    print("toisella pizzalla on pienempi yksikköhinta.")
else:
    print("pizzoilla sama yksikköhinta.")