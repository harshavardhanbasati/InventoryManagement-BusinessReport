-- =========================================
-- INVENTORY REPORT
-- =========================================

SELECT
    p.product_name,
    i.quantity,
    p.price,
    i.quantity * p.price AS inventory_value
FROM inventory i
JOIN products p
    ON i.product_id = p.product_id
ORDER BY inventory_value DESC;


-- =========================================
-- LOW STOCK REPORT
-- =========================================

SELECT
    p.product_id,
    p.product_name,
    i.quantity
FROM inventory i
JOIN products p
    ON i.product_id = p.product_id
WHERE i.quantity <= 10
ORDER BY i.quantity ASC;


-- =========================================
-- TOTAL SALES
-- =========================================

SELECT
    COALESCE(
        SUM(quantity * unit_price),
        0
    ) AS total_sales
FROM sale_items;


-- =========================================
-- TOP SELLING PRODUCTS
-- =========================================

SELECT
    p.product_name,
    SUM(si.quantity) AS units_sold,
    SUM(
        si.quantity * si.unit_price
    ) AS revenue
FROM sale_items si
JOIN products p
    ON si.product_id = p.product_id
GROUP BY
    p.product_id,
    p.product_name
ORDER BY units_sold DESC;


-- =========================================
-- SALES BY CATEGORY
-- =========================================

SELECT
    c.category_name,
    SUM(si.quantity) AS units_sold,
    SUM(
        si.quantity * si.unit_price
    ) AS revenue
FROM sale_items si
JOIN products p
    ON si.product_id = p.product_id
JOIN categories c
    ON p.category_id = c.category_id
GROUP BY
    c.category_id,
    c.category_name
ORDER BY revenue DESC;


-- =========================================
-- MONTHLY SALES
-- =========================================

SELECT
    DATE_TRUNC('month', s.sale_date) AS month,
    SUM(
        si.quantity * si.unit_price
    ) AS revenue
FROM sales s
JOIN sale_items si
    ON s.sale_id = si.sale_id
GROUP BY month
ORDER BY month;