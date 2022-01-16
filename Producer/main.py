import time
from random import randint

from kafka import KafkaProducer

from producer import Producer
from serializers import json_serializer
from user_event_generator import generate_user


def main() -> None:
    kafka_producer = KafkaProducer(
        bootstrap_servers=["localhost:9092"], value_serializer=json_serializer
    )

    producer = Producer(kafka_producer, "users")

    # TODO: Podmienić wartości w forze i w time na consty/configi
    for i in range(1, 1000):
        producer.send_message(generate_user())
        time.sleep(randint(1, 5))


if __name__ == "__main__":
    main()
