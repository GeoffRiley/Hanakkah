-- SQLite

-- SELECT c.customerid, name, phone, 
--  SUBSTR(name, INSTR(name, ' ')+1) AS last_name
-- -- orderid, ordered, shipped
--  FROM customers c 
--  INNER JOIN orders o ON c.customerid = o.customerid
--  WHERE SUBSTR(name, 1, 1) = 'J' AND SUBSTR(name, INSTR(name, ' ')+1, 1) = 'P'
--  GROUP BY last_name, o.ordered
--  ORDER BY last_name, o.ordered
-- -- HAVING (STRFTIME('%Y',ordered)) = 2017
-- ;

-- SELECT name, c.customerid, address, phone, 
--  STRFTIME('%Y',MIN(ordered)) AS first_order, 
--  STRFTIME('%Y',MAX(ordered)) AS last_order
--  FROM customers c 
--  INNER JOIN orders o ON c.customerid = o.customerid
--  WHERE SUBSTR(name, 1, 1) = 'J' AND
--   SUBSTR(name, INSTR(name, ' ')+1, 1) = 'P'
--  GROUP BY name
--  ORDER BY last_order DESC
-- ;

-- SELECT *
-- FROM products
-- WHERE desc LIKE '%offee%' or desc LIKE '%agel%'
-- ;
-- -- BKY1573 BKY5717 DLI8820

-- SELECT oi.orderid, COUNT(oi.sku) AS items, c.name, c.phone
-- FROM orders_items oi
-- INNER JOIN orders o ON oi.orderid = o.orderid
-- INNER JOIN customers c ON o.customerid = c.customerid
-- WHERE sku IN ('BKY1573', 'BKY5717', 'DLI8820') AND
--  SUBSTR(name, 1, 1) = 'J' AND
--  SUBSTR(name, INSTR(name, ' ')+1, 1) = 'P'
-- GROUP BY oi.orderid 
-- HAVING COUNT(oi.sku) > 1 
-- ORDER BY items DESC
-- ;
-- Contractor found: (7459, 2, 'Joshua Peterson', '332-274-4185')
-- SELECT *
-- FROM customers
-- WHERE name = 'Joshua Peterson' AND phone = '332-274-4185'
-- ;
-- customerid: 1475
-- name: Joshua Peterson
-- address: 100-75 148th St
-- citystatezip: Jamaica, NY 11435
-- birthdate: 1947-02-05
-- phone: 332-274-4185
-- timezone: America/New_York
-- lat: 40.70895
-- long: -73.80856


-- Check if birthdate is for a astrological Cancer
-- that is between June 21 and July 22
-- Check also that the year is one of the Chinese zodiac years
-- of the Rabbit. 1927, 1939, 1951, 1963, 1975, 1987, 1999, 2011
-- SELECT *
-- FROM customers
-- WHERE STRFTIME('%m%d', birthdate) >= '0621' AND
--  STRFTIME('%m%d', birthdate) <= '0722' AND 
--  STRFTIME('%Y', birthdate) IN ('1927', '1939', '1951', '1963', '1975', '1987', '1999', '2011') AND
--  SUBSTR(citystatezip,1,3) = 'Jam'
-- ;
-- customerid: 2550
-- name: Robert Morton
-- address: 145-51 107th Ave
-- citystatezip: Jamaica, NY 11435
-- birthdate: 1999-07-08
-- phone: 917-288-9635
-- timezone: America/New_York
-- lat: 40.68959
-- long: -73.80487

-- Woman made multiple purchases of pastries before 5am
-- SELECT c.name, c.phone, COUNT(oi.sku) as items
-- FROM orders_items oi
-- INNER JOIN orders o ON oi.orderid = o.orderid
-- INNER JOIN customers c ON o.customerid = c.customerid
-- WHERE sku LIKE 'BKY%' AND
--   STRFTIME('%H%m', shipped) < '0500'
--   GROUP BY c.customerid
--     HAVING COUNT(oi.sku) > 2
-- ;
 
 