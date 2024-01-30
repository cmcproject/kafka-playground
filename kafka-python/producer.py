import time
import json
from datetime import datetime
from data_generator import generate_message
from kafka import KafkaProducer


def serializer(message: dict):
    return json.dumps(message).encode("utf-8")


producer = KafkaProducer(
    bootstrap_servers=["localhost:9092"],
    value_serializer=serializer,
)

if __name__ == "__main__":
    while True:
        dummy_message = generate_message()
        print(f"{datetime.now()}: Producing message {dummy_message}")
        producer.send(topic="messages", value=dummy_message)
        time.sleep(5)
