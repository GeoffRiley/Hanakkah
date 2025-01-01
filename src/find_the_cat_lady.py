import hoc_data.hoc_connect


def find_the_cat_lady(database_path):
    conn = hoc_data.hoc_connect.Database(database_path)
    cursor = conn.conn.cursor()

    query = """
            WITH cte AS (
                SELECT c.name,
                    c.phone,
                    c.customerid,
                    COUNT(oi.sku) AS items,
                    DENSE_RANK() OVER (ORDER BY COUNT(oi.sku) DESC) AS rnk
                FROM customers c
                JOIN orders o ON c.customerid = o.customerid
                JOIN orders_items oi ON o.orderid = oi.orderid
                JOIN products p ON oi.sku = p.sku
                WHERE citystatezip LIKE 'Staten Island%'
                AND UPPER(desc) LIKE '%CAT%'
                GROUP BY c.customerid
            )
            SELECT name, phone, items
            FROM cte
            WHERE rnk = 1;
        """
    cursor.execute(query)

    result = cursor.fetchall()

    conn.conn.close()

    return result


def main():
    database_path = ""
    if cat_ladies := find_the_cat_lady(database_path):
        for cat_lady in cat_ladies:
            print(f"Cat lady found: {cat_lady}")
        print(f"Found {len(cat_ladies)} cat ladies.")
    else:
        print("Cat lady not found.")


if __name__ == "__main__":
    main()

# Cat lady found: ('Nicole Wilson', '631-507-6048', 21)
# Cat lady found: ('Brian Hudson III', '516-570-4577', 21)
# Brian isn't a lady, so we disregard him. Nicole Wilson is the cat lady.
