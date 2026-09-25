-- =========================
-- CATEGORIES
-- =========================

INSERT INTO categories (category_name)
VALUES
    ('Electronics'),
    ('Furniture'),
    ('Stationery'),
    ('Accessories');


-- =========================
-- SUPPLIERS
-- =========================

INSERT INTO suppliers (supplier_name, email, phone)
VALUES
    ('TechWorld Supplies', 'techworld@example.com', '9876543210'),
    ('OfficeMart', 'officemart@example.com', '9876543211'),
    ('Smart Accessories', 'smartaccessories@example.com', '9876543212');


-- =========================
-- PRODUCTS
-- =========================

INSERT INTO products
    (product_name, category_id, supplier_id, price)
VALUES
    ('Laptop', 1, 1, 65000.00),
    ('Wireless Mouse', 1, 1, 1200.00),
    ('Keyboard', 1, 1, 1800.00),
    ('Office Chair', 2, 2, 8500.00),
    ('Office Table', 2, 2, 12000.00),
    ('Notebook', 3, 2, 120.00),
    ('Pen Pack', 3, 2, 250.00),
    ('USB Cable', 4, 3, 450.00);


-- =========================
-- INVENTORY
-- =========================

INSERT INTO inventory (product_id, quantity)
VALUES
    (1, 10),
    (2, 50),
    (3, 30),
    (4, 15),
    (5, 8),
    (6, 100),
    (7, 75),
    (8, 60);


-- =========================
-- CUSTOMERS
-- =========================

INSERT INTO customers (customer_name, email, phone)
VALUES
    ('Rahul Kumar', 'rahul@example.com', '9000000001'),
    ('Priya Sharma', 'priya@example.com', '9000000002'),
    ('Arjun Reddy', 'arjun@example.com', '9000000003');


-- =========================
-- SAMPLE SALES
-- =========================

INSERT INTO sales (customer_id)
VALUES
    (1),
    (2);


-- =========================
-- SALE ITEMS
-- =========================

INSERT INTO sale_items
    (sale_id, product_id, quantity, unit_price)
VALUES
    (1, 1, 1, 65000.00),
    (1, 2, 2, 1200.00),
    (2, 3, 1, 1800.00),
    (2, 6, 5, 120.00);