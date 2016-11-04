# Note Younes Bannany: De initialize basis
# -- Flask toegevoegd
# -- Static routing toegevoegd, web folder toegevoegd
# -- Favicon toegevoegd
# -- Rest api basis toegevoegd

# Note Lars Van Kleef: Tweede versie
# -- Api uitgebreid met controller
# -- Api verder gemaakt

from flask import *
from database import db

from controllers import userController, bikeController, shedController

app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
    return send_from_directory('web/static', "index.html")

@app.route('/static/<path:path>')
def resolveStaticFiles(path):
    '''Laat de website zien'''
    return send_from_directory('web/static', path)

@app.route('/api/user/register', methods=['POST'])
def registerUser():
    '''Registeer een gebruiker in het systeem'''
    if not request.json or not 'first_name' in request.json:
        abort(400)

    user = userController.addUser(request.json)

    return jsonify(user), 201


@app.route('/api/user/id/<firstname>/<lastname>')
def getUserId(firstname, lastname):
    '''Vind de gebruiker door middel van zijn voor en achternaam'''
    user = userController.getUser({
        'first_name': firstname,
        'last_name': lastname
    })

    return jsonify(user), 200


@app.route('/api/user/bikes/<userId>')
def getBiksById(userId):
    '''Bekijk alle fietsen van een gebruiker'''
    bikes = bikeController.getBikes({
        'user_id': userId
    })

    return jsonify(bikes), 200


@app.route('/api/bike/shedhistroy/<bikeUid>')
def getShedHistory(bikeUid):
    '''bekijk het verleden van een fiets'''
    shedHistory = shedController.getShedHistory({
        'bike_uid': bikeUid
    })

    return jsonify(shedHistory), 200


@app.route('/api/bike/register', methods=['POST'])
def registerBike():
    '''registreer een fiets aan een gebruiker'''
    if not request.json or not 'user_id' in request.json:
        abort(400)

    bike = bikeController.addBikeToUser(request.json)

    return jsonify(bike), 201

@app.route('/api/shed/add', methods=['POST'])
def addBikeToShed():
    '''Zet een fiets in de stalling'''
    if not request.json or not 'bike_uid' in request.json:
        abort(400)

    inshed = shedController.addBikeToShed(request.json)

    return jsonify(inshed), 200

@app.route('/api/shed/remove', methods=['POST'])
def removeBikeFromShed():
    '''Haal een fiets weer uit de stalling'''
    if not request.json or not 'bike_uid' in request.json:
        abort(400)

    outShed = shedController.removeBikeFromShed(request.json)

    return jsonify(outShed), 200

@app.route('/api/places')
def getShedPlaces():
    '''Kijk hoeveel stal plaatsen er nog over zijn het zijn er in totaal 1500'''
    places = shedController.getFreePlaces()

    return jsonify(places), 200

if __name__ == '__main__':
    db.createDb()
    app.run(debug=True)
