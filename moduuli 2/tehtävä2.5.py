leiviskä = float(input("Anna leiviskät: "))
naula = float(input("Anna naulat: "))
luoti = float(input("Anna luodit: "))

luotipaino = 13.3*luoti
naulapaino = naula*(32*13.3)
leiviskäpaino = leiviskä*(20*(32*13.3))

kilot = float((luotipaino + naulapaino + leiviskäpaino)//1000)
grammat = float((luotipaino + naulapaino + leiviskäpaino) % 1000)

print("Massa nykymittojen mukaan:" '\n' + str(kilot) + "kg ja " + str(grammat) + "g." )