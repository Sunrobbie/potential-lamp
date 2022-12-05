import sqlite3

con = sqlite3.connect("BaseStation.sqb");

cur = con.cursor()

res =  cur.execute("SELECT Callsign, Firstlat, Lastlat, Firstlon, Lastlon FROM Flights WHERE Callsign IS NOT '';");

#res = cur.execute("SELECT table_name FROM all_tables ORDER BY table_name ASC;")

print(res.fetchall())

res = cur.execute("SELECT Registration FROM Aircraft WHERE Registration LIKE Raytheon")

print(res.fetchall())

con.close()