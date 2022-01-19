from kafka import KafkaProducer
import json
producer = KafkaProducer(bootstrap_servers='127.0.0.1:9093', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# producer.send('usertopic', b'hi')
producer.send('usertopic', {'email': 'user@gmail.com'})
producer.flush()