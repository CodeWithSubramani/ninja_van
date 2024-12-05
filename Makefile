start:
	docker compose -f docker-compose-debezium.yml up -d --build && \
	docker compose -f docker-compose-kafka.yml up -d --build && \
	cd airflow/docker && \
	docker compose up -d --build && \
	docker exec -it docker-airflow-webserver-1 sh -c "pip install pyarrow"
	python3 src/inventory_consumer.py


stop:
	docker compose -f docker-compose-debezium.yml down -v && \
	docker compose -f docker-compose-kafka.yml down -v && \
	cd airflow/docker -v && \
	docker compose down -v

