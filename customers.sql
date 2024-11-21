SELECT customer_name, COUNT(sale_id) AS purchase_count
FROM sales
JOIN customers ON sales.customer_id = customers.customer_id
GROUP BY customer_name
ORDER BY purchase_count DESC;
