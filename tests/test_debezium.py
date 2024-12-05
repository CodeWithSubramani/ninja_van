import requests


def test_add_connector():
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


def test_get_connectors():
    url = f"http://localhost:8083/connectors"
    response = requests.get(url=url)
    data = response.json()
    pass


def test_get_connector():
    connector_name = 'inventory-connector'
    connector_name = 'authentication-connector'
    url = f"http://localhost:8083/connectors/{connector_name}"
    response = requests.get(url=url)
    data = response.json()
    pass


def test_delete_connector():
    # connector_name = 'inventory-connector'
    connector_name = 'authentication-connector'
    url = f"http://localhost:8083/connectors/{connector_name}"
    response = requests.delete(url=url)
    data = response.json()
    pass
