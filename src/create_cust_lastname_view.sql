-- SQLite
CREATE VIEW customers_last_name AS
SELECT customerid, name, phone, SUBSTR(name, INSTR(name, ' ')+1) AS last_name
FROM customers where length(last_name) == 10;
