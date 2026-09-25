-- =========================
-- INDEXES
-- =========================

CREATE INDEX idx_products_category
ON products(category_id);

CREATE INDEX idx_products_supplier
ON products(supplier_id);

CREATE INDEX idx_inventory_product
ON inventory(product_id);

CREATE INDEX idx_sales_customer
ON sales(customer_id);

CREATE INDEX idx_sales_date
ON sales(sale_date);

CREATE INDEX idx_sale_items_sale
ON sale_items(sale_id);

CREATE INDEX idx_sale_items_product
ON sale_items(product_id);