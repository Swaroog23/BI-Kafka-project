class Producer:
    def __init__(self, kafka_producer, topic) -> None:
        self.kafka_producer = kafka_producer
        self.topic = topic

    def send_message(self, message) -> None:
        print("sending message: ", message)
        self.kafka_producer.send(self.topic, message)
