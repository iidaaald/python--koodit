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