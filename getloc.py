#!/usr/bin/python
import mysqlinit
import MySQLdb
import MySQLdb.cursors

ipaddress = mysqlinit.get_lan_ip()
user = mysqlinit.user()
password = mysqlinit.password()
ipaddress = mysqlinit.get_lan_ip()
cnx = MySQLdb.connect(user=user, passwd=password, host='127.0.0.1', db='automation',cursorclass=MySQLdb.cursors.DictCursor)
cursor=cnx.cursor()

cursor.execute("""SELECT latitude,longitude FROM location ORDER BY id DESC  limit 1""")
row = cursor.fetchone()
lat = row['latitude']
lon = row['longitude']

json_string = '{"lat":' + '"' + str(lat) + '", "lon":' + '"' + str(lon) + '"}'
print "Content-Type:applicatiaon/json\r\n"
print json_string
