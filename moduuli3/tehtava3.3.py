sukupuoli = input("Anna sukupuoli: ")
hemo = float(input("Anna hemoglobiinin arvo: "))

if sukupuoli == "nainen":
    if 117<=hemo<=175:
        print("Naisen hemoglobiiniarvo on normaali.")
    elif hemo<117:
         print("Naisen hemoglobiiniarvo on alhainen.")
    elif hemo>175:
        print("Naisen hemoblobiiniarvo on korkea.")
if sukupuoli == "mies":
    if 134 <= hemo <= 195:
        print("Miehen hemoglobiiniarvo on normaali.")
    elif hemo < 134:
        print("Miehen hemoglobiiniarvo on alhainen.")
    elif hemo > 195:
        print("Miehen hemoblobiiniarvo on korkea.")

