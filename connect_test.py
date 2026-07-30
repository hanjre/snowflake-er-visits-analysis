import os
import getpass
import snowflake.connector

password = getpass.getpass("Snowflake password: ")

conn = snowflake.connector.connect(
    account=os.getenv("SNOWFLAKE_ACCOUNT", "UZSDACD-JZ99935"),
    user=os.getenv("SNOWFLAKE_USER", "HANJRE"),
    password=password,
    warehouse=os.getenv("SNOWFLAKE_WAREHOUSE", "COMPUTE_WH"),
    database=os.getenv("SNOWFLAKE_DATABASE", "PORTFOLIO_DB"),
    schema=os.getenv("SNOWFLAKE_SCHEMA", "ANALYTICS")
)

cur = conn.cursor()

try:
    cur.execute("""
        SELECT
            CURRENT_USER(),
            CURRENT_ACCOUNT_NAME(),
            CURRENT_WAREHOUSE(),
            CURRENT_DATABASE(),
            CURRENT_SCHEMA()
    """)
    print(cur.fetchone())
finally:
    cur.close()
    conn.close()