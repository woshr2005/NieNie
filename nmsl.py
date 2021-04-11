# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
import pandas
import mysql.connector
username = str("Jun@atsspec.com")
password = str("Xj325489761")
DBhost = str("read-only-db-replica.cdj1pnsllfod.us-east-1.rds.amazonaws.com")
DBusername = str("data.jun")
DBpassword = str("Xj325489761")
DBname = str("atsspec_net")

def cookie_to_dict(cookie):
    cookie_dict = {}
    items = cookie.split(';')
    for item in items:
        key = item.split('=')[0].replace(' ', '')
        value = item.split('=')[1]
        cookie_dict[key] = value
    return cookie_dict
session = requests.Session()
payload = {'usernameLogin': username, 'rawPwdLogin': password, 'username': username, 'password': password, 'platform': 'Project Tracker'}
r = session.post('https://atsapi.com/auth/v1/login', data=payload)
print(r.text)
a = r.text
for i in a:
    b = a.split("\"")
toc= b[-2]
print(toc)
session = requests.Session()
payload = {'token': toc, 'login': 'Login'}
r = session.post('https://atsspec.com/user/index/login/spec/project', data=payload)
print(r.cookies.get_dict())
mydb = mysql.connector.connect(
  host=DBhost,
  user=DBusername,
  passwd=DBpassword,
  database=DBname)                   
mycursor = mydb.cursor()
mycursor.execute("SELECT s.`id` FROM spec s JOIN drawing d ON s.`id` = d.`spec_id` JOIN drawing_fixture df ON d.`id` = df.`drawing_id` JOIN fixture fx ON df.`fixture_id` = fx.`id` JOIN `user` u ON s.`creator_id` = u.`id` JOIN firm f ON u.`firm_id` = f.`id` JOIN manufacturer m ON fx.`manufacturer_id` = m.`id` LEFT JOIN drawing_custom dc ON d.`id` = dc.`drawing_id` AND m.`id` = dc.`manufacturer_id` WHERE s.`status_id` = 1 AND u.`status_id` =1 AND f.`status_id` =1 AND f.`firm_type_id` NOT IN (9,20) AND s.`spec_type_id` IN (1,2) AND df.`is_another` = 0 AND d.`status_id` IN (1,11)     AND (DATE(s.`created`) >='2019-01-01' OR DATE(s.`modified`) >='2019-01-01') AND m.`status_id` IN (1,27) AND m.id NOT IN (74,52,583,7) AND f.`id` NOT IN (10667) GROUP BY s.`id` HAVING(COUNT(df.id)>COUNT(dc.`id`)) ORDER BY s.`id` DESC;")
myresult = mycursor.fetchall()
df = pandas.DataFrame({'Spec id':myresult})
for i in df['Spec id']:
    print (i[0])
    url = 'https://atsspec.com/crm/spec/run-drawing-custom'
    payload = {'specId': str(i[0])}
    r = session.post(url, data = payload)
    print(r.text)