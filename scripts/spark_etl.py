import json
import psycopg2

with open("/opt/airflow/data_lake/raw_user.json") as f:
    data = json.load(f)

user = data["results"][0]

conn = psycopg2.connect(
    host="postgres",
    database="airflow",
    user="airflow",
    password="airflow"
)

cursor = conn.cursor()

cursor.execute(
    """
    INSERT INTO users_data (first_name, last_name, gender, country, email)
    VALUES (%s, %s, %s, %s, %s)
    """,
    (
        user["name"]["first"],
        user["name"]["last"],
        user["gender"],
        user["location"]["country"],
        user["email"],
    ),
)

conn.commit()
cursor.close()
conn.close()

print("Data loaded into PostgreSQL")