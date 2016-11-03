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
    user = userController.getUser({'first_name': firstname,
                                   'last_name': lastname})

    return jsonify(user), 200

@app.route('/api/bike/register', methods=['POST'])
def registerBike():
    if not request.json or not 'user_id' in request.json:
        abort(400)

    bike = bikeController.addBikeToUser(request.json)

    return jsonify(bike), 201

@app.route('/api/shed/add', methods=['POST'])
def addBikeToShed():
    if not request.json or not 'bike_uid' in request.json:
        abort(400)

    inshed = shedController.addBikeToShed(request.json)

    return jsonify(inshed), 201

@app.route('/api/shed/remove', methods=['POST'])
def removeBikeFromShed():
    if not request.json or not 'bike_uid' in request.json:
        abort(400)

    outShed = shedController.removeBikeFromShed(request.json)

    return jsonify(outShed), 201

if __name__ == '__main__':
    db.createDb()
    app.run(debug=True)
