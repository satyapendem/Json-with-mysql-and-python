import pymysql

conn=pymysql.connect(host="localhost",    
                     user="root",         
                     passwd="root",  
                     db="satya")

cursor = conn.cursor()

cursor.execute("SELECT * FROM data")
values = cursor.fetchall()
for row in values:
    print row[1]
    print row[2]



conn.close()