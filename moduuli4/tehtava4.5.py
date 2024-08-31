kayttaja = input("Käyttäjätunnus: ")
salasana = input("Salasana: ")

oikeakayttaja = "python"
oikeasalasana = "rules"
i = 0

while (kayttaja or salasana) != "":
    if i < 5:
        if (kayttaja == oikeakayttaja) and (salasana == oikeasalasana):
            print("Tervetuloa!")
            break
        if kayttaja != oikeakayttaja:
            print("Väärä käyttäjä.")
            kayttaja = input("Anna käyttäjätunnus uudelleen: ")
            i = i +1
        if salasana != oikeasalasana:
            print("Väärä salasana.")
            salasana = input("Anna salasana uudelleen: ")
            i = i +1
    else:
        print("Pääsy evätty")
        break