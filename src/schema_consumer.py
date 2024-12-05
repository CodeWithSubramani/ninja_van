import json
import os
from datetime import datetime

from kafka import KafkaConsumer

if __name__ == '__main__':
    consumer = KafkaConsumer(
        "dbserver1.inventory.customers",
        bootstrap_servers="localhost:9092",
        group_id="unique_group_id",
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    )

    for message in consumer:
        timestamp = datetime.now()
        file_path = (f'../data/events_store/{timestamp.year}/{timestamp.month}/{timestamp.day}/{timestamp.hour}'
                     f'/{timestamp.minute}')

        os.makedirs(file_path, exist_ok=True)
        file_name = f"event_{message.timestamp}.json"
        file_full_path = os.path.join(file_path, file_name)
        with open(f"{file_full_path}", "w") as f:
            json.dump(message.value, f)
