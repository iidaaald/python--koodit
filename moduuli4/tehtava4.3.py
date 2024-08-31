i = input("Anna luku: ")
suurin = i
pienin = i

while i != "":
    uusi = input("Anna toinen luku: ")
    if uusi == "":
        break
    if uusi > suurin:
        suurin = uusi
    if uusi < pienin:
        pienin = uusi
print(f"suurin luku on {suurin}. Pienin luku on {pienin}.")
