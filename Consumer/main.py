import json
from consumer import Consumer

from kafka import KafkaConsumer

if __name__ == "__main__":
    kafka_consumer = KafkaConsumer(
        "users",
        bootstrap_servers=["localhost:9092"],
        auto_offset_reset="earliest",
        group_id="user-consumers",
    )

    consumer = Consumer(kafka_consumer)
    consumer.start_consuming()
