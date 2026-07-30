import getpass
import snowflake.connector

password = getpass.getpass("Snowflake password: ")

conn = snowflake.connector.connect(
    account="UZSDACD-JZ99935",
    user="HANJRE",
    password=password,
    warehouse="COMPUTE_WH",
    database="PORTFOLIO_DB",
    schema="ANALYTICS"
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