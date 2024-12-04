docker run -d \
  --name=zookeeper \
  --network=kafka_network \
  -p 2181:2181 \
  wurstmeister/zookeeper:3.4.6

docker run -d \
  --name=kafka \
  --network=kafka_network \
  -p 9093:9093 \
  -e KAFKA_ADVERTISED_LISTENER=PLAINTEXT://localhost:9093 \
  -e KAFKA_LISTENER_SECURITY_PROTOCOL=PLAINTEXT \
  -e KAFKA_LISTENER_PORT=9093 \
  -e KAFKA_ZOOKEEPER_CONNECT=zookeeper:2181 \
  wurstmeister/kafka:latest

docker run -d \
  --name=debezium-connector \
  --link=kafka \
  --link=zookeeper \
  -e "BOOTSTRAP_SERVERS=kafka:9093" \
  -e "CONNECT_REST_PORT=8083" \
  -e "CONNECT_GROUP_ID=debezium" \
  -e "CONNECT_CONFIG_STORAGE_TOPIC=my-connect-configs" \
  -e "CONNECT_OFFSET_STORAGE_TOPIC=my-connect-offsets" \
  -e "CONNECT_STATUS_STORAGE_TOPIC=my-connect-status" \
  -e "CONNECT_KEY_CONVERTER=org.apache.kafka.connect.storage.StringConverter" \
  -e "CONNECT_VALUE_CONVERTER=io.debezium.converters.AvroConverter" \
  debezium/connect:1.9
