'''
Created on 2018年4月23日

@author: xielin
'''
# -*- coding: utf-8 -*-
import cx_Oracle

con = cx_Oracle.connect('slview/slview@192.168.6.173:1521/dbnms') #1个参数

#conn = cx_Oracle.connect('slview', 'slview', '192.168.6.173:1521/173DBNMS') #3个参数

cursor = con.cursor()
sql = "SELECT d.username,decrypt_data(d.password,'beijingtiananmen')password FROM device d "
cursor.execute(sql)  
row = cursor.fetchall()
#print (row)
cursor.close()  
con.close()
with open("data/user.txt","w") as f:
    f.write(row)
f.close()
