import json
import os
from datetime import datetime

from kafka import KafkaConsumer


def test_schema_consumer_debugging():
    consumer = KafkaConsumer(
        "dbserver1.inventory.customers",
        bootstrap_servers="localhost:9092",
        group_id="debugger",
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    )

    # Local directory for storing events (change this to your desired location)
    timestamp = datetime.now()
    base_dir = (f'../../data/events_store/{timestamp.year}/{timestamp.month}/{timestamp.day}/{timestamp.hour}'
                f'/{timestamp.minute}')

    # Time interval for batching events (for example: every 5 minutes)
    batch_interval = 5  # in minutes

    # Buffer to store events
    events_buffer = []

    # Timestamp to track the batch timing
    last_batch_time = datetime.now()

    # Process the incoming Kafka messages
    for message in consumer:
        # Append the event to the buffer
        events_buffer.append(message.value)

        # Check if the batch interval has passed (every 5 minutes in this case)
        current_time = datetime.now()
        if (current_time - last_batch_time).total_seconds() >= batch_interval * 60:
            # Create a timestamp-based directory structure for file storage
            timestamp = current_time
            file_dir = os.path.join(base_dir,
                                    f"{timestamp.year}/{timestamp.month}/{timestamp.day}/{timestamp.hour}/{timestamp.minute}/")
            os.makedirs(file_dir, exist_ok=True)

            # Create a file name based on the timestamp
            file_name = f"events_batch_{timestamp.strftime('%Y%m%d_%H%M%S')}.json"
            file_full_path = os.path.join(file_dir, file_name)

            # Write events buffer to file
            with open(file_full_path, "w") as file:
                json.dump(events_buffer, file, indent=4)

            print(f"Written {len(events_buffer)} events to {file_full_path}")

            # Clear the buffer after writing to file
            events_buffer = []

            # Reset the last batch time
            last_batch_time = current_time

    print("Consumer stopped")
