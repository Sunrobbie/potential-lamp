import sqlite3

con = sqlite3.connect("BaseStation.sqb");

cur = con.cursor()

res =  cur.execute("SELECT * FROM Flights");

#res = cur.execute("SELECT table_name FROM all_tables ORDER BY table_name ASC;")

print(res.fetchall())

con.close()