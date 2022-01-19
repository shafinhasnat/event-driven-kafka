from kafka import KafkaConsumer, TopicPartition
import json
import time

consumer = KafkaConsumer(
    bootstrap_servers=['127.0.0.1:9093'],
    auto_offset_reset='latest',
    group_id="usergroup",
    enable_auto_commit=True,
)

def latestStream():
    consumer.subscribe('usertopic')
    for msg in consumer:
        resp = json.loads(msg.value.decode('UTF-8'))
        print('Sending Email to: ' + resp['email'])
        time.sleep(1)
        print('---> Email sent to: ' + resp['email'])

def latestWithPrev():
    topic_partition = TopicPartition("usertopic", 0)
    assigned_topic = [topic_partition]
    consumer.assign(assigned_topic)
    consumer.commit()
    for msg in consumer:
        resp = json.loads(msg.value.decode('UTF-8'))
        print('Sending Email to: ' + resp['email'])
        time.sleep(1)
        print('---> Email sent to: ' + resp['email'])

latestWithPrev()