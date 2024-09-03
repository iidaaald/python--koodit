
#def listan_summa(lista):
 #   return sum(lista)
def listan_summa(lista):
    sum = 0
    for i in range(len(lista)):
        sum =  sum + lista[i]
    return sum

luvut = [2, 3, 1,6]
summa = listan_summa(luvut)
print(summa)