from hoc_data.hoc_connect import Database


def find_contractor(database_path, contractor_initials):
    conn = Database(database_path)
    cursor = conn.conn.cursor()

    query = """
            SELECT oi.orderid, COUNT(oi.sku) AS items, c.name, c.phone
            FROM orders_items oi
            INNER JOIN orders o ON oi.orderid = o.orderid
            INNER JOIN customers c ON o.customerid = c.customerid
            WHERE sku IN ('BKY1573', 'BKY5717', 'DLI8820') AND
            SUBSTR(name, 1, 1) = ? AND
            SUBSTR(name, INSTR(name, ' ')+1, 1) = ?
            GROUP BY oi.orderid 
            HAVING COUNT(oi.sku) > 1 
            ORDER BY items DESC
            ;
        """
    # query = "SELECT * FROM customers c WHERE SUBSTR(name,1,1) = ?"  # AND STRFTIME('%Y',shipped) = ? AND c.customerid = o.customerid"
    cursor.execute(query, (contractor_initials[0], contractor_initials[1]))

    result = cursor.fetchall()

    conn.conn.close()

    return result


if __name__ == "__main__":
    database_path = ""
    contractor_initials = "JP"
    if contractors := find_contractor(database_path, contractor_initials):
        for contractor in contractors:
            print(f"Contractor found: {contractor}")
        print(f"Found {len(contractors)} contractors.")
    else:
        print("Contractor not found.")

# Contractor found: (7459, 2, 'Joshua Peterson', '332-274-4185')
