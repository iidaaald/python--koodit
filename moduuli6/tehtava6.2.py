#Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän.
# Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
# Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan
# nopan maksimisilmäluku, joka kysytään käyttäjältä ohjelman suorituksen alussa.

import random

maksimi = int(input("Anna nopan maksimisilmäluku: "))

def nopanheitto(maksimi):
    while True:
        tulos = int(random.randint(1,maksimi))
        print(tulos)
        if tulos == maksimi:

            return


nopanheitto(maksimi)
