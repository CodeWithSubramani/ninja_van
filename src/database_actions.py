import secrets

import psycopg2

conn_params = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "postgres",
    "host": "localhost",
    "port": "5433"
}


def test_insert_data_inventory():
    conn = psycopg2.connect(**conn_params)
    cursor = conn.cursor()
    random_str = secrets.token_hex(3)
    insert_query = f"""
    INSERT INTO inventory.customers (first_name, last_name, email)
    VALUES
        ('{random_str}', '{random_str + "_l"}', '{random_str + "@test.com"}');
    """
    cursor.execute(insert_query)
    conn.commit()
    cursor.close()
    conn.close()
