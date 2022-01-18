# KAFKA Made easy

### Commands:

Image and Documentation link: [bitnami kafka](https://hub.docker.com/r/bitnami/kafka/)

`docker-compose up -d`

## Kafka cli:

### Using kafka inside the container

`docker exec -it <KAFKA_SERVER_CONTAINER> /bin/sh`

`cd opt/bitnami/kafka/bin`

This location holds all `.sh` files for kafka cli

##### Create new topic

`kafka-topics.sh --create --bootstrap-server kafka:9092 --replication-factor 1 --partitions 1 --topic <TOPIC_NAME>`

##### List all topics

`kafka-topics.sh --list --bootstrap-server kafka:9092`

##### Produce Message to topic
`kafka-console-producer.sh --broker-list kafka:9092 --topic usertopic`

##### Consume Message from topic
`kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic usertopic --from-beginning`

### Using kafka outside the container
We are using `kafka-python` as our kafka client for python.

##### Produce Message to a topic
 ```python
 from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='127.0.0.1:9093')
producer.send('usertopic', b'Message from Python')
producer.flush()
 ```