import sqlite3
import matplotlib.pyplot as plt

con = sqlite3.connect("BaseStation.sqb");

cur = con.cursor()

#res =  cur.execute("SELECT Callsign, Firstlat, Lastlat, Firstlon, Lastlon FROM Flights WHERE Callsign IS NOT ''");

#res = cur.execute("SELECT table_name FROM all_tables ORDER BY table_name ASC;")

#print(res.fetchall())

res =  cur.execute("SELECT Callsign, Firstlat, Lastlat, Firstlon, Lastlon, FirstGroundSpeed, LastGroundSpeed FROM Flights");

allFlights = res.fetchall()

flightSpeeds = list(filter(lambda item: item[5] is not None and item[6] is not None, allFlights))

flightSpeeds = list(map(lambda item: item[5], flightSpeeds)) + list(map(lambda item: item[6], flightSpeeds))

plt.figure()

for flight in allFlights:
    x = (flight[1], flight[2])
    y = (flight[3], flight[4])
    plt.plot(x, y)

plt.figure()


plt.hist(flightSpeeds)

plt.figure()

res = cur.execute("SELECT AircraftID FROM Aircraft WHERE Manufacturer LIKE 'Raytheon%'")

militaryId = res.fetchall()

print(militaryId)

queryM = "SELECT Callsign, Firstlat, Lastlat, Firstlon, Lastlon FROM Flights WHERE AircraftID in(%s)"

res =  cur.execute(queryM % "'59', '561', '599'")

militData = res.fetchall()

for flight in militData:
    x = (flight[1], flight[2])
    y = (flight[3], flight[4])
    plt.plot(x, y)



con.close()