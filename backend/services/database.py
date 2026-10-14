import os
import psycopg2

# Connection string matching your Docker configuration
DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql://admin:admin@localhost:5432/appdb"
)

try:
    # 1. Establish connection to the database
    connection = psycopg2.connect(DATABASE_URL)
    cursor = connection.cursor()

    # 2. Execute a lightweight query to check responsiveness
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()

    print("Connection successful!")
    print(f"Postgres Version: {db_version[0]}")

except Exception as error:
    print(f"Connection failed: {error}")

finally:
    # 3. Ensure resources are properly released
    if "connection" in locals() and connection:
        cursor.close()
        connection.close()
