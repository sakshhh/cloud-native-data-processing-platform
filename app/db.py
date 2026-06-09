import os
import psycopg2

from dotenv import load_dotenv

load_dotenv()

def get_connection():

    return psycopg2.connect(
        host=os.getenv("POSTGRES_HOST"),
        port=os.getenv("POSTGRES_PORT"),
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
    )


def save_report(filename, result):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO processed_reports
        (
            filename,
            total_employees,
            average_salary,
            total_salary
        )
        VALUES (%s,%s,%s,%s)
        """,
        (
            filename,
            result["total_employees"],
            result["average_salary"],
            result["total_salary"]
        )
    )

    conn.commit()

    cursor.close()
    conn.close()