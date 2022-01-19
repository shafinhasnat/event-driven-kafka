import pymongo
from kafka import KafkaConsumer
import json
import time

consumer = KafkaConsumer(bootstrap_servers='127.0.0.1:9093')
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
consumer.subscribe('usertopic')
    
mydb = myclient["eda"]
mycol = mydb["user"]

for msg in consumer:
    resp = json.loads(msg.value.decode('UTF-8'))
    mycol.insert_one(resp)
    print('New entry done: ' + resp['email'])
