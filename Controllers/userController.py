from Database import db

def addUser(requestData):
    try:
        user = db.addUser(
            requestData['first_name'],
            requestData['middel_name'],
            requestData['last_name'],
            requestData['address'],
            requestData['zipcode'],
            requestData['city']
        )

        return {
            'success': 1,
            'user_id': int(user[0][0]),
            'first_name': user[0][1],
            'middel_name': user[0][2],
            'last_name': user[0][3],
            'address': user[0][4],
            'zipcode': user[0][5],
            'city': user[0][6]
        }
    except:
        return {
            'success': 0
        }