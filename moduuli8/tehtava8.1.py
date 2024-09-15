#Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin.
# Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen ja sen
# sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta.
# ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen.

import mysql.connector

def get_airport_by_icao(icao):
    sql = f'SELECT name, municipality FROM airport where ident = "{icao}"'
    #print (sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos


yhteys = mysql.connector.connect(
    host= 'localhost',
    port=3306,
    database= 'flight_game',
    user= 'iida',
    password= 'Omena1ohko',
    autocommit= True
)

koodi = input("Lentoaseman ICAO-koodi: ")

joo = get_airport_by_icao(koodi)
print(f'Nimi on: {joo[0][0]} sijaintikunta on : {joo[0][1]}')





