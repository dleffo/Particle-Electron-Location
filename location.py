#!/usr/bin/python
import cgi
import cgitb
import time
import mysqlinit
import MySQLdb
import MySQLdb.cursors
import dateutil.parser
import dateutil.tz

cgitb.enable()
ipaddress = mysqlinit.get_lan_ip()
form = cgi.FieldStorage()
user = mysqlinit.user()
password = mysqlinit.password()
ipaddress = mysqlinit.get_lan_ip()
cnx = MySQLdb.connect(user=user, passwd=password, host='127.0.0.1', db='automation',cursorclass=MySQLdb.cursors.DictCursor)
cursor=cnx.cursor()

event = form.getfirst("event", "GPS")
data = form.getfirst("data","01,01")
published_at = form.getfirst("published_at",'01-01-01T01:01:01')
coreid = form.getfirst("coreid","test")
lat,lon = data.split(",")
d = dateutil.parser.parse(published_at, ignoretz=True)

cursor.execute('''INSERT INTO location (latitude,longitude,coreid,datetime) VALUES('%s','%s','%s','%s')''' % (lat,lon,coreid,d))
cnx.commit()


print "Content-Type:text/html\r\n\r\n"
print "Success!"
print event
print data
print published_at
print coreid
print lat
print lon
print d
