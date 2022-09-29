INSERT INTO seller_info(seller_id, fruit_id, fruit_weight, id)
VALUES (1, 3, 5, 1),
(7, 3, 3, 2),
(2,3,3.1,3),
(12,1,2.1,4),
(1,1,12,5),
(2,1,12,6)

INSERT INTO consumption_info(fruit_id, seller_id, client_id, quantity_purchased_fruit, id)
VALUES (1, 3, 5, 2, 1),
(5, 1, 2, 1, 2),
(1,3,1, 17, 3),
(2,6,21,2, 4),
(12,3,2,7, 5),
(1,11,12,4, 6)

SELECT * FROM consumption_info

SELECT * FROM seller_info

SELECT AVG(sums) FROM (
SELECT SUM(fruit_weight) as sums FROM seller_info
GROUP BY seller_id) as g_s


SELECT COUNT(*) FROM (
SELECT seller_id FROM consumption_info
GROUP BY seller_id HAVING SUM(quantity_purchased_fruit) > 0
) as g

SELECT COUNT(*) FROM (
SELECT seller_id FROM consumption_info
GROUP BY seller_id HAVING COUNT(seller_id) > 0
) as g