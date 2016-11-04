# Note Lars van Kleef: De initialize basis
# -- Maken eerste versies van elke functie om de data op te slaan

# Note Younes Bannany:
# -- Werkend gemaakt, type verwijderd

import sqlite3
import string
import random
import time
import os

conn = sqlite3.connect(str(os.path.dirname(__file__))+'/Data/ns.sqlite', check_same_thread = False)


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def createDb():
    '''This will create a sqlite3 database'''
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS bikes
             (id INTEGER PRIMARY KEY AUTOINCREMENT, uid INTEGER, user_id INTEGER)''')

    c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY AUTOINCREMENT, first_name TEXT, insertion TEXT, last_name Text, address TEXT, zip_code TEXT, city TEXT, UNIQUE (first_name, last_name))''')

    c.execute('''CREATE TABLE IF NOT EXISTS shed
             (id INTEGER PRIMARY KEY AUTOINCREMENT, bike_id INTEGER, start_time DATE, end_time DATE)''')

    c.execute('''CREATE TABLE IF NOT EXISTS places
             (id INTEGER PRIMARY KEY AUTOINCREMENT, places BIGINT)''')


def addUser(first_name='null', insertion='null', last_name='null', address='null', zip_code='null', city='null'):
    c = conn.cursor()

    try:
        c.execute("INSERT INTO users (first_name, insertion, last_name, address, zip_code, city) "
                  "VALUES ('"+str(first_name)+"','"+str(insertion)+"','"+str(last_name)+"','"+str(address)+"','"+str(zip_code)+"','"+str(city)+"')")
        conn.commit()
        return getUserByFirstAndLastName(first_name, last_name)

    except:
        return False


def getUserByFirstAndLastName(first_name, last_name):
    c = conn.cursor()

    try:
        c.execute("SELECT * FROM users WHERE first_name = '"+str(first_name)+"' AND last_name = '"+str(last_name)+"'")
        return c.fetchall()

    except:
        return False


def addBikeToUser(userId):
    c = conn.cursor()

    try:
        uid = id_generator()
        c.execute("INSERT INTO `bikes`(`uid`,`user_id`) VALUES ('" + str(uid) + "'," + str(userId) + ")")
        conn.commit()
        return (uid, userId)

    except:
        print('Er is iets mis gegaan!')


def getBikeByUid(uid):
    c = conn.cursor()

    try:
        c.execute("SELECT * FROM bikes WHERE uid = '" + uid + "'")
        return c.fetchone()

    except:
        return False


def getBikeByUserId(userId):
    c = conn.cursor()

    try:
        c.execute("SELECT * FROM users WHERE id = '"+str(userId)+"'")
        return c.fetchall()

    except:
        return False


def getBikesFromUser(userId):
    c = conn.cursor()

    try:
        c.execute("SELECT * FROM bikes WHERE user_id = '" + str(userId) + "'")

        return c.fetchall()
    except:
        return False


def addBikeToShed(bikeId):
    c = conn.cursor()
    now = int(time.time())

    try:
        c.execute("INSERT INTO shed (bike_id, start_time, end_time) VALUES ('"+str(bikeId)+"', '"+str(now)+"', 'NULL')")
        conn.commit()
        return True

    except:
        return False


def removeBikeFromShed(bikeId):
    c = conn.cursor()
    now = int(time.time())

    try:
        c.execute("UPDATE shed SET end_time = '"+str(now)+"' WHERE bike_id = '"+bikeId+"'")
        conn.commit()
        return True

    except:
        return False


def removeFreePlace():
    '''Fiets word gestald er word dus een vrije plaats weggehaald'''
    c = conn.cursor()

    try:
        c.execute("SELECT * FROM places")
        places = c.fetchall()

        if len(places) >= 1:
            counter = int(places[0][1])
            c.execute("UPDATE places SET places = '"+str(counter + 1) +"' WHERE id = 1")
            conn.commit()
        else:
            c.execute("INSERT INTO places (places) VALUES (1)")
            conn.commit()
        return True

    except:
        return True

def addFreePlace():
    '''Fiets word opgehaald dus er is weer een nieuwe vrije plaats'''
    c = conn.cursor()

    try:
        c.execute("SELECT *) FROM places")
        places = c.fetchall()
        if len(places) >= 1:
            counter = int(places[0][1])
            c.execute("UPDATE places SET places = '"+str(counter - 1) +"' WHERE id = 1")
            conn.commit()
        else:
            c.execute("INSERT INTO places (places) VALUES (0)")
            conn.commit()
        return True

    except:
        return False

def getShedHistory(bikeUid):
    c = conn.cursor()

    try:
        c.execute("SELECT * FROM shed WHERE bike_uid = '"+bikeUid+"'")
        return c.fetchall()
    except:
        return False

def getPlaces():
    c = conn.cursor()

    try:
        c.execute("SELECT * FROM places")
        places = c.fetchone()
        return places

    except:
        return False


