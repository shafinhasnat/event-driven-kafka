from kafka import KafkaConsumer
import json
import time
consumer = KafkaConsumer(bootstrap_servers='127.0.0.1:9093')
consumer.subscribe('usertopic')

for msg in consumer:
    resp = json.loads(msg.value.decode('UTF-8'))
    print('Sending Email to: ' + resp['email'])
    time.sleep(1)
    print('Email sent to: ' + resp['email'])
