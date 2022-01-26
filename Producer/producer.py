import time
from random import randint
from validators import (
    validate_delay,
    validate_number_of_events,
    validate_strings_are_numeric,
)

from user_event_generator import generate_user
from kafka import KafkaProducer


class Producer:
    def __init__(self, topic, kafka_producer) -> None:
        self.topic = topic
        self.kafka_producer = kafka_producer
        self.min_delay = None
        self.max_delay = None
        self.num_of_events = None

    def generate_events(self) -> None:
        for i in range(int(self.num_of_events)):
            message = generate_user()
            self.kafka_producer.send(self.topic, message)
            time.sleep(randint(int(self.min_delay), int(self.max_delay)))

    def set_event_parameters(self):
        num_of_events = input("Number of events (max 100 thousand): ")
        min_delay = input("Minimal delay: ")
        max_delay = input("Maximal delay: ")

        try:
            validate_strings_are_numeric([num_of_events, min_delay, max_delay])
            self.num_of_events = int(num_of_events)
            self.max_delay = int(max_delay)
            self.min_delay = int(min_delay)
        except ValueError as error:
            raise error

    def send_events(self):
        self.set_event_parameters()
        self.validate_event_params()
        self.generate_events()

    def validate_event_params(self):
        if not None in (self.max_delay, self.min_delay, self.num_of_events):
            try:
                validate_delay(self.min_delay, self.max_delay)
                validate_number_of_events(self.num_of_events)
            except ValueError as error:
                raise error
        else:
            raise TypeError("Parameters are None!")
