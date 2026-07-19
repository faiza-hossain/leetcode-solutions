SELECT t.product_id, IFNULL(p.new_price, 10) AS price
FROM (
    SELECT DISTINCT product_id
    FROM Products
) t
LEFT JOIN Products p
    ON p.product_id = t.product_id
    AND p.change_date = (
        SELECT MAX(change_date)
        FROM Products
        WHERE product_id = t.product_id
        AND change_date <= '2019-08-16'
    )
ORDER BY t.product_id;