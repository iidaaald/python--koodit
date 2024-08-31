import random
pist_maara = int(input("Arvottavien pisteiden määrä: "))

while pist_maara != "":
    x = random.randint (-1,1)
    y = random.randint (1, -1)
    if x **2 + y **2<1:
