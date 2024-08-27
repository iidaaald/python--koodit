alamitta = 37
kuhanpituus = float(input("Anna kuhan pituus senttimetreinä: "))
erotus = alamitta - kuhanpituus

if kuhanpituus < alamitta:
    print("laske kuha takaisin järveen.")
    print(f"Kuhan pituudesta puuttuu: {erotus:5.3f} senttimetriä.")
if kuhanpituus >= alamitta:
    print("hyvän kokoinen kuha!")
