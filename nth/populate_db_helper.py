import sqlite3
import csv

with open('airports.csv', 'r') as f:
    reader = list(csv.reader(f))
    sql = sqlite3.connect('../app.db')
    cur = sql.cursor()
    cur.execute('DROP TABLE IF EXISTS airports')
    cur.execute('''CREATE TABLE IF NOT EXISTS airports
                (ident text,
                type text,
                name text,
                coordinates text,
                elevation_ft text,
                continent text,
                iso_country text,
                iso_region text,
                municipality text,
                gps_code text,
                iata_code text,
                local_code text)''')  # create the table if it doesn't already exist

    for row in reader[1:]:
        cur.execute(u"INSERT INTO airports VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", [x.decode('utf-8') for x in row])

    sql.commit()
    sql.close()
