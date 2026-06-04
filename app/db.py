import psycopg2

def get_connection():

    return psycopg2.connect(
        host="postgres",
        port=5432,
        database="dataplatform",
        user="admin",
        password="admin"
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