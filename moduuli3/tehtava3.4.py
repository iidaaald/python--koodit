#Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi.
# Vuosi on karkausvuosi, jos se on jaollinen neljällä. Sadalla jaolliset vuodet ovat karkausvuosia
# vain jos ne ovat jaollisia myös neljälläsadalla.
vuosiluku = float(input("Mikä vuosiluku?: "))

ehto = vuosiluku % 4 == 0
ehto2 = vuosiluku % 100 != 0
ehto3 = vuosiluku % 400 == 0

if (ehto and ehto2) or ehto3:
        print("Vuosi on karkausvuosi.")
else:
        print("Vuosi ei ole karkausvuosi.")
