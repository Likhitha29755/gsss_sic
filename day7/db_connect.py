'''
import pymysql

def Connect_db():
    conn = pymysql.Connect(host='localhost',user='root',password='Likhi@123' , database='likhitha_db',port=3306,charset='utf8')
    return conn

connection=Connect_db()
if connection:
    print('Database Connected')
else:
    print('Database Connection failed')


connection.close()
print('Database disconnected')
#connection.close()
'''

#OR

import pymysql

def Connect_db():
    try: 
        conn = pymysql.Connect(host='localhost',user='root',password='Likhi@123' , database='likhitha_db',port=3306,charset='utf8')    #if we give wrong password it print except block.
        print('Database Connected')
        return conn
    except:
         print('Database Connection failed')

connection=Connect_db()
if connection:
    connection.close()
    print('Database disconnected')
