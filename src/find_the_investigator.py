import sqlite3


def fetch_customers_last_name(db_path):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Execute the query to fetch data from the view
    cursor.execute("SELECT * FROM customers_last_name")

    # Fetch all rows from the executed query
    rows = cursor.fetchall()

    # Close the connection
    conn.close()

    return rows


if __name__ == "__main__":
    db_path = "/home/geoffr/dev/Hanakkah/data/5784/noahs.sqlite"
    customers_last_name = fetch_customers_last_name(db_path)
    trs = str.maketrans(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "22233344455566677778889999", "()',"
    )
    for row in customers_last_name:
        cust_num, cust_name, cust_phone, cust_lastname = row
        cust_match = cust_lastname.upper().translate(trs)
        cust_match = f"{cust_match[:3]}-{cust_match[3:6]}-{cust_match[6:]}"
        if cust_match == cust_phone:
            print(f"{cust_num}: {cust_name:25} {cust_phone} {cust_match}")

# 1208: Sam Tannenbaum            826-636-2286 826-636-2286
