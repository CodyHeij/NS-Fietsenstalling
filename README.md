# NS-Fietsenstalling

## Docs

### createDb
Deze functie moet een keer uit gevoerd worden in main.py. Hier door word er een database gemaakt met de juiste tabellen.

### addUser
Maak een gebruiker aan in de database

- first_name (str)
- insertion (str)
- last_name (str)
- address (str)
- zip_code (str)
- city (str)

Deze functie geeft als alles goed gaat de de aan gemaakte user terug.

### getUserByFirstAndLastName
Deze functie geeft de gebruiker terug met de gegeven voor en achternaam.

- first_name (str)
- last_name (str)

### addBikeToUser
Koppel fiets aan een gebruiker er word automatische een uniqeu code gemaakt. 

- userId (int)

Deze functie geeft als alles goed gaat de userid en de bikeUid terug.

### getBikeByUid
Vind een fiets bij uid. Met deze functie kun je kijken of een fiets in de stalling is.

- bike_uid (str)

Deze functie geeft de fiets info terug.

### getBikesFromUser
Laat alle fietsen van een gebruiker zien.

- userId (int)

Deze functie geeft als alles goed gaat een lijst met fietsen terug (als de gebruiker meerder fietsen heeft)

### addBikeToShed
**bike id is iets anders als een bike_uid**
Voeg een fiets toe aan de stalling. Er word een start tijd opgeslagen. Later bij het ophalen word er een eind tijd aan gemaakt.

- bikeId (int)
- userId (str)

Geeft True als het gelukt is en False als het mis gegaan is.

### removeBikeFromShed
**bike id is iets anders als een bike_uid**
Zet een eindtijd bij een fiets stalling zo dat hier na een tijd between kan worden uit gerekend.

- bikeId (int)