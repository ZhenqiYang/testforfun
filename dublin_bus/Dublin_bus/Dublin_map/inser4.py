import csv
import mysql.connector

cnx = mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='steve003',
    db='dublin_bus',


)

cursor = cnx.cursor()

with open('bus_locations.csv') as csv_file:
    csv_data = csv.reader(csv_file, delimiter=',')

    for row in csv_data:
        cursor.execute('INSERT INTO dublin_map_bus_locations (stop_id,  stop_name,  latitude, longitude) \
            VALUES(%s, %s, %s, %s)',
                       row)

    cnx.commit()
    cursor.close()
print("Done")