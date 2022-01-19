from kafka import KafkaConsumer
import json
consumer = KafkaConsumer(bootstrap_servers='127.0.0.1:9093')
consumer.subscribe('usertopic')

for msg in consumer:
    resp = json.loads(msg.value.decode('UTF-8'))
    print(resp['email'])
