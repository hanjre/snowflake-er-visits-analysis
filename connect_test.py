from config import get_connection

conn = get_connection()
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