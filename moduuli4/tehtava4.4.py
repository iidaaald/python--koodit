#Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10. Kone arvuuttelee lukua
# pelaajalta siihen asti, kunnes tämä arvaa oikein. Kunkin arvauksen jälkeen ohjelma tulostaa
# tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein. Huomaa, että tietokone ei saa
# vaihtaa lukuaan arvauskertojen välissä.

import random

rando =  (random.randint(1,10))
arvaus = float(input("Arvaa numero 1:n ja 10:n väliltä: "))

while arvaus != "":
    if arvaus == rando:
        print("Oikein!")
        break
    if arvaus > rando:
        print("Liian suuri arvaus.")
        arvaus = float(input("Arvaa uudestaan: "))
    if arvaus < rando:
        print("Liian pieni arvaus.")
        arvaus = float(input("Arvaa uudestaan: "))