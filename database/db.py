# Note Lars van Kleef: De initialize basis
# -- Maken eerste versies van elke functie om de data op te slaan

# Note Younes Bannany:
# -- Werkend gemaakt, type verwijderd

# Note Lars van Kleef: Tweede versie
# -- extra functies toegevoegd zo dat de rest van de site meer data heeft om te gebruiken.

import sqlite3
import string
import random
import time
import os

conn = sqlite3.connect(str(os.path.dirname(__file__))+'/Data/ns.sqlite', check_same_thread = False)


def id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def createDb():
    '''Dit stuk maakt een sqlite database aan'''
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS bikes
             (id INTEGER PRIMARY KEY AUTOINCREMENT, uid INTEGER, user_id INTEGER)''')

    c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY AUTOINCREMENT, uid INTEGER, first_name TEXT, insertion TEXT, last_name Text, address TEXT, zip_code TEXT, city TEXT, UNIQUE (first_name, last_name))''')

    c.execute('''CREATE TABLE IF NOT EXISTS shed
             (id INTEGER PRIMARY KEY AUTOINCREMENT, bike_id INTEGER, start_time DATE, end_time DATE)''')

    c.execute('''CREATE TABLE IF NOT EXISTS places
             (id INTEGER PRIMARY KEY AUTOINCREMENT, places BIGINT)''')

    c.execute('''INSERT INTO places (places) VALUES (0)''')
    conn.commit()


def addUser(first_name='null', insertion='null', last_name='null', address='null', zip_code='null', city='null'):
    '''Met deze functie kun je een gebruiker aanmaken'''
    c = conn.cursor()

    try:
        uid = id_generator()
        c.execute("INSERT INTO users (uid, first_name, insertion, last_name, address, zip_code, city) "
                  "VALUES ('"+str(uid)+"','"+str(first_name)+"','"+str(insertion)+"','"+str(last_name)+"','"+str(address)+"','"+str(zip_code)+"','"+str(city)+"')")
        conn.commit()
        return getUserByFirstAndLastName(first_name, last_name)

    except:
        return False


def getUserByFirstAndLastName(first_name, last_name):
    '''Met deze functie kun je een gebruiker zoeken met zijn voor en achternaam'''
    c = conn.cursor()

    try:
        c.execute("SELECT * FROM users WHERE first_name = '"+str(first_name)+"' AND last_name = '"+str(last_name)+"'")
        return c.fetchall()

    except:
        return False


def addBikeToUser(userId):
    '''Voeg een fiets toe aan een gebruiker'''
    c = conn.cursor()

    try:
        uid = id_generator()
        c.execute("INSERT INTO `bikes`(`uid`,`user_id`) VALUES ('" + str(uid) + "'," + str(userId) + ")")
        conn.commit()
        return (uid, userId)

    except:
        print('Er is iets mis gegaan!')


def getBikeByUid(uid):
    '''Zoek een fiets bij zijn uid'''
    c = conn.cursor()

    try:
        c.execute("SELECT * FROM bikes WHERE uid = '" + uid + "'")
        return c.fetchone()

    except:
        return False

def getBikesFromUser(userId):
    '''Krijg een lijst met alle fietsen van een een gebruiker'''
    c = conn.cursor()

    try:
        c.execute("SELECT * FROM bikes WHERE user_id = '" + str(userId) + "'")
        return c.fetchall()

    except:
        return False


def addBikeToShed(bikeId):
    '''Stal een fiets'''
    c = conn.cursor()
    now = int(time.time())

    try:
        c.execute("INSERT INTO shed (bike_id, start_time, end_time) VALUES ('"+str(bikeId)+"', datetime("+str(now)+", 'unixepoch', 'localtime'), 'NULL')")
        conn.commit()
        return True

    except:
        return False


def removeBikeFromShed(bikeId):
    '''Haal een fiets op'''
    c = conn.cursor()
    now = int(time.time())

    try:
        c.execute("UPDATE shed SET end_time = datetime("+str(now)+", 'unixepoch', 'localtime') WHERE bike_id = '"+str(bikeId)+"' AND end_time = 'NULL'")
        conn.commit()

        print('veranderd')
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
        c.execute("SELECT * FROM places")
        places = c.fetchall()
        if len(places) >= 1:
            counter = int(places[0][1])
            if not counter <= 0:
                c.execute("UPDATE places SET places = '"+str(counter - 1) +"' WHERE id = 1")
                conn.commit()
        else:
            c.execute("INSERT INTO places (places) VALUES (0)")
            conn.commit()
        return True

    except:
        return False

def getShedHistory(bikeId):
    '''Bekijk alle stallingen van vroeger'''
    c = conn.cursor()

    c.execute("SELECT * FROM shed WHERE id = '"+str(bikeId)+"'")
    return c.fetchall()

def getPlaces():
    '''bekijk hoeveel plaatsen er nog zijn'''
    c = conn.cursor()

    try:
        c.execute("SELECT * FROM places")
        places = c.fetchone()
        return places

    except:
        return False


