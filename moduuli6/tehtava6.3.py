#Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina
# ja palauttaa paluuarvonaan vastaavan litramäärän. Kirjoita pääohjelma,
# joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi.
# Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka,
# kunnes käyttäjä syöttää negatiivisen gallonamäärän.
#Yksi gallona on 3,785 litraa.

galloonia = float(input("Gallonmäärä: "))
def muunnos(galloonia):
    tulos = galloonia * 3.785
    return tulos

while galloonia > 0:
    print(f"{muunnos(galloonia)} litraa")
    galloonia = float(input("Gallonmäärä: "))
