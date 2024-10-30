'''
Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api. Kirjoita ohjelma,
joka kysyy käyttäjältä paikkakunnan nimen ja tulostaa sitä vastaavan säätilan tekstin sekä lämpötilan
 Celsius-asteina. Perehdy rajapinnan dokumentaatioon riittävästi. Palveluun rekisteröityminen on tarpeen,
 jotta saat rajapintapyynnöissä tarvittavan API-avaimen (API key). Selvitä myös, miten saat Kelvin-asteet
  muunnettua Celsius-asteiksi.
'''
import requests
paikkakunta = input("Anna paikkakunnan nimi: ")
key = "a6b72d0e6c578c6812c479596738097e"
pyyntö = f"http://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&units=metric&appid={key}"
try:
    vastaus = requests.get(pyyntö).json()

    #sää
    sää = vastaus["weather"][0]["description"]
    #lämpötila
    lämpötila = vastaus["main"]["temp"]

    print(f"{paikkakunta}: {sää}")
    print(f"Lämpötila: {lämpötila}°C")

except requests.exceptions.RequestException as cod:
    print("Error")