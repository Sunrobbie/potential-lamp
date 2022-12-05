import sqlite3
import matplotlib.pyplot as plt

con = sqlite3.connect("BaseStation.sqb");

cur = con.cursor()

res =  cur.execute("SELECT Callsign, Firstlat, Lastlat, Firstlon, Lastlon FROM Flights WHERE Callsign IS NOT ''");

#res = cur.execute("SELECT table_name FROM all_tables ORDER BY table_name ASC;")

print(res.fetchall())

res = cur.execute("SELECT AircraftID FROM Aircraft WHERE Manufacturer LIKE 'Raytheon%'")

militaryId = res.fetchall()

print(militaryId)

queryM = "SELECT Callsign, Firstlat, Lastlat, Firstlon, Lastlon FROM Flights WHERE AircraftID in(%s)"

res =  cur.execute(queryM % "'59', '561', '599'")

militData = res.fetchall()

for flight in militData:
    x = (flight[1], flight[1][2])
    y = (flight[3], flight[1][4])

plt.plot(x, y)

con.close()