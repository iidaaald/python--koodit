'''
Toteuta taustapalvelu, joka palauttaa annettua lentokentän ICAO-koodia vastaavan lentokentän
 nimen ja kaupungin JSON-muodossa. Tiedot haetaan opintojaksolla käytetystä lentokenttätietokannasta.
  Esimerkiksi EFHK-koodia vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/kenttä/EFHK.
  Vastauksen on oltava muodossa: {"ICAO":"EFHK", "Name":"Helsinki Vantaa Airport", "Municipality":"Helsinki"}.
'''
from flask import Flask, Response, jsonify
import mysql.connector

yhteys = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='iida',
    password='Omena1ohko',
    autocommit=True
)

app = Flask(__name__)


@app.route('/kenttä/<koodi>')
def get_airport_by_icao(icao):
    try:
        sql = f'SELECT name, municipality FROM airport where ident = "{icao}"'
        kursori = yhteys.cursor()
        kursori.execute(sql)
        tulos = kursori.fetchall()
        return tulos
    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virhe"
        }


def lentokentän_nimi(koodi):
    try:
        joo = get_airport_by_icao(koodi)
        tilakoodi = 200
        vastaus = {
            "ICAO": koodi,
            "Name": joo[0][0],
            "Municipality": joo[0][1],
        }

    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virhe"
        }
        return jsonify(vastaus), 200

    #jsonvast = json.dumps(vastaus)
    #return Response(response=jsonvast, status=tilakoodi, mimetype="application/json")


@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status": "404",
        "teksti": "Virheellinen päätepiste"
    }
    return jsonify(vastaus), 404



if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
