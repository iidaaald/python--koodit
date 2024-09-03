#Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan
# silmäluvun väliltä 1..6.Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen.
# Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.

import random

def nopanheitto():
    while True:
        tulos = int(random.randint(1,6))
        print(tulos)
        if tulos == 6:
            return


nopanheitto()

