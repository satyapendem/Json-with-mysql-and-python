import requests
import json
from pprint import pprint
import pymysql

conn=pymysql.connect(host="localhost",    
                     user="root",         
                     passwd="root",  
                     db="satya")#### Function to connect with mysql DB

link=open("demo.json")
#requests.get("http://roadtrippers.herokuapp.com/api/v1/cities/")##loads the json from the link

data=json.load(link)


#pprint(data)
cur=conn.cursor()
for i in range(0,len(data["cities"])):
	x=data["cities"][i]
	ids= x['id']
	names=x['name']
	covers=x['cover']
	states=x['state']
	cur.execute("INSERT INTO data (ID,NAME,COVER,STATE) \
      VALUES (%s , %s , %s , %s)",(ids,names,covers,states));

print "********JSON DATA LOADED TO TABLE*********"
     
conn.commit() 
conn.close()