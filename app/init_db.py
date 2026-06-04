import time
from app.db import get_connection


def create_table():

    conn = None

    for attempt in range(10):
        try:
            conn = get_connection()
            print("Connected to PostgreSQL")
            break

        except Exception as e:
            print(f"Attempt {attempt + 1}: PostgreSQL not ready")
            time.sleep(3)

    if conn is None:
        raise Exception("Could not connect to PostgreSQL")

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS processed_reports (
            id SERIAL PRIMARY KEY,
            filename VARCHAR(255),
            total_employees INTEGER,
            average_salary NUMERIC,
            total_salary NUMERIC,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    conn.commit()

    cursor.close()
    conn.close()