import hoc_data.hoc_connect


def find_the_early_bird(database_path):
    conn = hoc_data.hoc_connect.Database(database_path)
    cursor = conn.conn.cursor()

    query = """
            SELECT c.name, c.phone, COUNT(oi.sku) as items
                FROM orders_items oi
                INNER JOIN orders o ON oi.orderid = o.orderid
                INNER JOIN customers c ON o.customerid = c.customerid
                WHERE sku LIKE 'BKY%' AND
                STRFTIME('%H%m', shipped) < '0500'
                GROUP BY c.customerid
                HAVING COUNT(oi.sku) > 2
                ;
        """
    cursor.execute(query)

    result = cursor.fetchall()

    conn.conn.close()

    return result


def main():
    database_path = ""
    if early_birds := find_the_early_bird(database_path):
        for early_bird in early_birds:
            print(f"Early bird found: {early_bird}")
        print(f"Found {len(early_birds)} early birds.")
    else:
        print("Early bird not found.")


if __name__ == "__main__":
    main()

# Early bird found: ('Renee Harmon', '607-231-3605', 5)
