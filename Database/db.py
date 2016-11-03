import sqlite3
import string
import random
import time
import os

conn = sqlite3.connect(str(os.path.dirname(__file__))+'/data/ns.db', check_same_thread = False)

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

def getBikesFromUser(userId):
    c = conn.cursor()

    try:
        c.execute("SELECT * FROM bikes WHERE user_id = '" + str(userId) + "'")

        return c.fetchone()
    except:
        return False

def addBikeToShed(bikeId):
    c = conn.cursor()
    now = int(time.time())

    try:
        c.execute("INSERT INTO shed (bike_id, start_time) VALUES ('"+str(bikeId)+"', '"+str(now)+"')")
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
