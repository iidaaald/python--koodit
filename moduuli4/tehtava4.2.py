i = float(input("anna tuumia: "))

kaava = i * 2.54
while i >= 0:
    kaava = i * 2.54
    print(f"Tuumat senttimetreinä {kaava:7.2f}")
    i = float(input("anna lisää tuumia: "))
print("Ei negatiivisa lukuja kiitos.")