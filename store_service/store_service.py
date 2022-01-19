import pymongo
from kafka import KafkaConsumer, TopicPartition
import json

consumer = KafkaConsumer(
    bootstrap_servers=['127.0.0.1:9093'],
    auto_offset_reset='latest',
    group_id="usergroup_store",
    enable_auto_commit=True,
)
topic_partition = TopicPartition("usertopic", 0)
assigned_topic = [topic_partition]
consumer.assign(assigned_topic)
consumer.commit()

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["eda"]
mycol = mydb["user"]

for msg in consumer:
    resp = json.loads(msg.value.decode('UTF-8'))
    mycol.insert_one(resp)
    print('New entry done: ' + resp['email'])
