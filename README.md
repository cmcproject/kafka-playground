# Kafka

- event streaming platform; enables users to collect, store, and process data to build real-time event-driven applications
- a single cluster is made up of brokers; broker handles producers and consumers and keeps data replicated in the cluster
- producer -> topic -> consumer

# Zookeeper

- used to manage a cluster, track status of nodes, maintain a list of topics and messages

# Cmds

## Run Kafka

- docker-compose -f docker-compose.yml up -d

## Topics

- cd /opt/kafka\_<version>/bin
- docker exec -it kafka /bin/sh
- kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic first_kafka_topic
- kafka-topics.sh --list --zookeeper zookeeper:2181
- kafka-topics.sh --describe --zookeeper zookeeper:2181 --topic dummy_topic
- kafka-topics.sh --delete --zookeeper zookeeper:2181 --topic dummy_topic

## Producer

- kafka-console-producer.sh --broker-list kafka:9092 --topic messages
  {'user_id': 1, 'recipiet_id': 2, 'message': 'Hi!'}
  {'user_id': 2, 'recipiet_id': 1, 'message': 'Bye!'}

## Consumer

- kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic messages
- kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic messages --from-beginning