# Simple Kafka setup using Docker and Python

# Steps

## Run Kafka and Zookeeper

- docker-compose -f docker-compose.yml up -d

## Topics

```
docker exec -it kafka /bin/sh

cd /opt/kafka_2.13-2.8.1/bin

kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic first_kafka_topic

kafka-topics.sh --list --zookeeper zookeeper:2181

kafka-topics.sh --describe --zookeeper zookeeper:2181 --topic dummy_topic

kafka-topics.sh --delete --zookeeper zookeeper:2181 --topic dummy_topic
```

## Producer

```
kafka-console-producer.sh --broker-list kafka:9092 --topic messages

{'user_id': 1, 'recipiet_id': 2, 'message': 'Hi!'}

{'user_id': 2, 'recipiet_id': 1, 'message': 'Bye!'}
```

## Consumer

```
kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic messages

kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic messages --from-beginning
```
