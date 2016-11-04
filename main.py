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
    return send_from_directory('web/static', path)

@app.route('/api/user/register', methods=['POST'])
def registerUser():
    if not request.json or not 'first_name' in request.json:
        abort(400)

    user = userController.addUser(request.json)

    return jsonify(user), 201


@app.route('/api/user/id/<firstname>/<lastname>')
def getUserId(firstname, lastname):
    user = userController.getUser({
        'first_name': firstname,
        'last_name': lastname
    })

    return jsonify(user), 200


@app.route('/api/user/bikes/<userId>')
def getBiksById(userId):
    '''Get all the bikes from the user'''
    bikes = userController.getBikes({
        'user_id': userId
    })

    return jsonify(bikes), 200


@app.route('/api/bike/shedhistroy/<bikeUid>')
def getShedHistory(userId):
    '''bekijk het verleden van een fiets'''
    shedHistory = shedController.getShedHistory({
        'user_id': userId
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

    return jsonify(inshed), 201

@app.route('/api/shed/remove', methods=['POST'])
def removeBikeFromShed():
    '''Haal een fiets weer uit de stalling'''
    if not request.json or not 'bike_uid' in request.json:
        abort(400)

    outShed = shedController.removeBikeFromShed(request.json)

    return jsonify(outShed), 201

@app.route('/api/places')
def getShedPlaces():
    '''Kijk hoeveel stal plaatsen er nog over zijn er zijn er in totaal 1500'''
    places = shedController.getFreePlaces()

    return jsonify(places), 200

if __name__ == '__main__':
    db.createDb()
    app.run(debug=True)
