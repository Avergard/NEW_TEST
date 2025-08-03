SELECT * FROM sellers;
SELECT id, name, age FROM sellers WHERE age = 42; -- вывод информации по возрасту

SELECT COUNT(*) FROM sellers; -- вывод количества всех продавцов

SELECT DISTINCT(id) FROM sellers; -- вывод всех позиций данной колонны

SELECT * FROM sellers WHERE sellers.sales IS NOT NULL ; -- проверка на нули

SELECT sales, COUNT(*)
FROM sellers
GROUP BY sales
HAVING COUNT(*) > 1; --проверка дубликатов

EXPLAIN ANALYZE SELECT * FROM sellers WHERE sales = 40; -- проверка производительности запроса

SELECT pg_size_pretty(pg_total_relation_size('sellers'));  -- проверка размера бд в кB