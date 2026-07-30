import os
import getpass
import snowflake.connector


def get_connection():
    password = getpass.getpass("Snowflake password: ")

    return snowflake.connector.connect(
        account=os.getenv("SNOWFLAKE_ACCOUNT", "UZSDACD-JZ99935"),
        user=os.getenv("SNOWFLAKE_USER", "HANJRE"),
        password=password,
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE", "COMPUTE_WH"),
        database=os.getenv("SNOWFLAKE_DATABASE", "PORTFOLIO_DB"),
        schema=os.getenv("SNOWFLAKE_SCHEMA", "ANALYTICS"),
    )