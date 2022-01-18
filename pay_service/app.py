from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='127.0.0.1:9093')
producer.send('usertopic', b'Message from Python')
producer.flush()