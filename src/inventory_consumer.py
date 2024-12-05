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
    print("Consumer Started")
    print(os.getcwd(), "current_path")

    for message in consumer:
        print("Received Message")
        print(message.value)
        timestamp = datetime.now()
        folder_path = f'data/events_store/unprocessed'

        os.makedirs(folder_path, exist_ok=True)
        file_name = f"event_{message.timestamp}.json"
        file_full_path = os.path.join(folder_path, file_name)
        with open(f"{file_full_path}", "w") as f:
            json.dump(message.value, f)
