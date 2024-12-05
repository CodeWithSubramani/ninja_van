# Steps to execute the project

Run the below command to start the application

```shell
make start
```

Try inserting dummy data into the database using the below command

```shell
python src/insert_mock_data.py
```

That's about it!

Reference URLs

1. Airflow
   http://localhost:8282/admin/airflow/tree?dag_id=ninja_van_micro_batch&num_runs=&root=
2. Kaka Topic
   http://localhost:9000/topic/dbserver1.inventory.customers/messages?partition=0&offset=0&count=100&keyFormat=DEFAULT&format=DEFAULT&isAnyProto=false

What is the application doing?

1. You should be able to see events passed to the kafka topic.
2. You should be able to see the event files come within the `data/unprocessed` folder
3. The airflow job is running every 1 minute. Which means within the next minute all the invidual event files will
   get appended into a group of records within the parquet file in the `data/processed` folder

Run the below command to stop the application (this removes all the data with it too)

```shell
make stop
```