from random import randint

from kafka import KafkaProducer

from producer import Producer
from serializers import json_serializer
from user_event_generator import generate_user


def main() -> None:
    kafka_producer = KafkaProducer(
        bootstrap_servers=["localhost:9092"], value_serializer=json_serializer
    )

    producer = Producer(topic="users", kafka_producer=kafka_producer)

    producer.send_events()


if __name__ == "__main__":
    main()
