SELECT product_name, SUM(quantity) AS total_sales
FROM sales
JOIN products ON sales.product_id = products.product_id
GROUP BY product_name
ORDER BY total_sales DESC;
