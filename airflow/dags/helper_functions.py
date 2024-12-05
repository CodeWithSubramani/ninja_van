import json
import os
import shutil
from datetime import datetime

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

# source_folder_path = "../../data/events_store/unprocessed"
# staging_folder_path = "../../data/events_store/staging"
# processed_folder_path = "../../data/events_store/processed"

source_folder_path = "/data/events_store/unprocessed"
staging_folder_path = "/data/events_store/staging"
processed_folder_path = "/data/events_store/processed"


def move_events_to_staging():
    files_ = os.listdir(source_folder_path)
    if not files_:
        return
    for event_file in files_:
        source_file_path = os.path.join(source_folder_path, event_file)
        target_file_path = os.path.join(staging_folder_path, event_file)
        shutil.move(source_file_path, target_file_path)


def get_combined_events_data():
    events_data = []
    files_ = os.listdir(staging_folder_path)
    if not files_:
        return
    for event_file in files_:
        target_file_path = os.path.join(staging_folder_path, event_file)
        with open(os.path.join(target_file_path), "r") as f:
            data = json.load(f)
            events_data.append(data)

    for event_file in os.listdir(staging_folder_path):
        os.remove(os.path.join(staging_folder_path, event_file))

    return events_data


def append_to_parquet(events_data, output_file):
    if not events_data:
        return
    combined_data = [event["payload"]["after"] for event in events_data if event["payload"]["before"] is None]
    if not combined_data:
        print("No new events to append.")
        return
    df = pd.DataFrame(combined_data)

    if os.path.exists(output_file):
        table = pa.Table.from_pandas(df)
        existing_table = pq.read_table(output_file)
        combined_table = pa.concat_tables([existing_table, table])
        pq.write_table(combined_table, output_file)
        print(f"Appended data to Parquet file: {output_file}")
    else:
        table = pa.Table.from_pandas(df)
        pq.write_table(table, output_file)
        print(f"Created new Parquet file: {output_file}")


def test_process_events():
    move_events_to_staging()
    events_data = get_combined_events_data()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"{processed_folder_path}/combined_events_{timestamp}.parquet"
    append_to_parquet(events_data, output_file)
