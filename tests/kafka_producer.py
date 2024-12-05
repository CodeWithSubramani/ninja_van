import json

from kafka import KafkaProducer

if __name__ == '__main__':
    print("starting kafka producer..")
    producer = KafkaProducer(
        bootstrap_servers="localhost:9092",
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    producer.send("orders", "order1")
    producer.flush()
    print("message produced")
