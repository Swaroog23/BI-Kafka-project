import json
from Database.db import insert_data

class Consumer:
    def __init__(self, kafka_consumer) -> None:
        self.kafka_consumer = kafka_consumer

    def consume_message(self, message) -> None:
        insert_data(json.loads(message))


    def start_consuming(self) -> None:
        for message in self.kafka_consumer:
            self.consume_message(message.value)
