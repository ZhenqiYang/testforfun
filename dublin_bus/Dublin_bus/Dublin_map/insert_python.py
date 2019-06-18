#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pandas as pd

import pymysql

# db = pymysql.connect("localhost", "testuser", "test123", "TESTDB", charset='utf8' )

db = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='steve003',
    db='dublin_bus',
    # charset='utf8'
)

# cursor = db.cursor()
#
# df = pd.read_csv('rt_trips_2017_I_DB_1000.txt', keep_default_na=True, sep=',\s+', delimiter=';',
#                  skipinitialspace=True)
# data = df
# for index, row in data.iterrows():
#     btitle1 = row['lineid']
#     bpub_date1 = "1688-09-25"
#     sql = "INSERT INTO dublin_map_bookinfo(btitle,bpub_date) VALUES ( '%s', '%s')"
#     data = (btitle1, bpub_date1)
#     cursor.execute(sql % data)
# db.commit()
    # try:
    #
    #     cursor.execute(sql % data)
    #
    #     db.commit()
    # except:
    #
    #     db.rollback()






#
# cursor = db.cursor()
#
# # df = pd.read_csv('bus_locations.csv', keep_default_na=True, sep=',\s+', delimiter=',',
# #                  skipinitialspace=True)
# df = pd.read_csv('bus_locations.csv', names=['stop_id','stop_name','latitude','longitude'], header=None)
#
# data = df
# print(data.head(5))
# for index, row in data.iterrows():
#     stop_id1 = row['stop_id']
#     stop_name1 = row["stop_name"]
#     latitude1=row['latitude']
#     longitude1=row['longitude']
#
#     sql = "INSERT INTO dublin_map_bus_locations (stop_id,stop_name,latitude,longitude) VALUES ( '%s', '%s','%s', '%s')"
#     data = (stop_id1,stop_name1,latitude1,longitude1)
#     cursor.execute(sql % data)
# db.commit()
#
#
#
#
#
#
#
# cursor = db.cursor()
#
# df = pd.read_csv('rt_trips_2017_I_DB_1000.txt', keep_default_na=True, sep=',\s+', delimiter=';',
#                  skipinitialspace=True)
# data = df
# for index, row in data.iterrows():
#     btitle1 = row['lineid']
#     bpub_date1 = "1688-09-25"
#     sql = "INSERT INTO dublin_map_bookinfo(btitle,bpub_date) VALUES ( '%s', '%s')"
#     data = (btitle1, bpub_date1)
#     cursor.execute(sql % data)
# db.commit()
#     try:
#
#         cursor.execute(sql % data)
#
#         db.commit()
#     except:
#
#         db.rollback()
#
#
#

#
# cursor.close()
# db.close()