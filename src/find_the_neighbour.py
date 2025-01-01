from hoc_data.hoc_connect import Database

# Camcer birth in year of Rabbit.
# The astrological sign of Cancer runs from June 21 to July 22.
# The Chinese zodiac sign of the Rabbit runs from February 19, 1999 to
# February 6, 2000,1 and then from February 7, 2011 to January 26, 2012. It
# repeats every 12 years.
# The Rabbit is the fourth sign of the Chinese zodiac.


def find_neighbour(database_path):
    conn = Database(database_path)
    cursor = conn.conn.cursor()

    query = """
            SELECT *
            FROM customers
            WHERE STRFTIME('%m%d', birthdate) >= '0621' AND
            STRFTIME('%m%d', birthdate) <= '0722' AND
            STRFTIME('%Y', birthdate) IN ('1927', '1939', '1951', '1963', '1975', '1987', '1999', '2011') AND
            SUBSTR(citystatezip,1,3) = 'Jam';
        """
    cursor.execute(query, ())

    result = cursor.fetchall()

    conn.conn.close()

    return result


if __name__ == "__main__":
    database_path = ""
    if neighbours := find_neighbour(database_path):
        for neighbour in neighbours:
            print(f"Neighbour found: {neighbour}")
        print(f"Found {len(neighbours)} neighbours.")
    else:
        print("Neighbour not found.")

# Neighbour found: (2550, 'Robert Morton', '145-51 107th Ave', 'Jamaica, NY 11435', '1999-07-08', '917-288-9635', 'America/New_York', 40.68959, -73.80487)
