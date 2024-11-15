'''
Toteuta Flask-taustapalvelu, joka ilmoittaa, onko parametrina saatu luku alkuluku
vai ei. Hyödynnä toteutuksessa aiempaa tehtävää, jossa alkuluvun testaus tehtiin.
Esimerkiksi lukua 31 vastaava GET-pyyntö annetaan
muodossa: http://127.0.0.1:3000/alkuluku/31. Vastauksen on oltava
muodossa: {"Number":31, "isPrime":true}.
'''
from flask import Flask, Response, jsonify

app = Flask(__name__)
@app.route('/alkuluku/<luku>')


def alkuluku(number):
    i = 1

    if number == 1 or number == 0:
        return False

    for n in range(2, number):
        if (number % n) == 0:
            i = i + 1
            break
    if i == 1:
        return True
    elif i == 2:
        return False


def tarkista(luku):
    try:
        number = int(luku)
        result = alkuluku(number)
        vastaus = {
            "Number": number,
            "isPrime": result
        }
        return jsonify(vastaus), 200

    except ValueError:
        vastaus = {
            "status": 400,
            "error": "Invalid input. Please provide an integer."
        }
        return jsonify(vastaus), 400

    except Exception as e:
        vastaus = {
            "status": 500,
            "error": f"An unexpected error occurred: {str(e)}"
        }
        return jsonify(vastaus), 500


@app.errorhandler(404)
def page_not_found(e):
    response_data = {
        "status": 404,
        "error": "Invalid endpoint. Please check the URL."
    }
    return jsonify(response_data), 404


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000)
