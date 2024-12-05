import requests


def test_register_debezium_postgres_connect():
    url = "http://localhost:8083/connectors"
    body = {
        "name": "inventory-connector",
        "config": {
            "connector.class": "io.debezium.connector.postgresql.PostgresConnector",
            "database.hostname": "postgres",
            "database.port": "5432",
            "database.user": "postgres",
            "database.password": "postgres",
            "database.dbname": "postgres",
            "database.server.name": "dbserver1",
            "table.include.list": "inventory.customers"
        }
    }
    response = requests.post(url=url, json=body)
    data = response.json()
    pass
