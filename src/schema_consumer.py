import json

from kafka import KafkaConsumer

if __name__ == '__main__':
    consumer = KafkaConsumer(
        "dbserver1.inventory.customers",
        bootstrap_servers="localhost:9092",
        group_id="unique_group_id",
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    )

    for message in consumer:
        print("Message received:")
        print(message.value)
