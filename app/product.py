from db import get_connection


# CREATE
def add_product(name, category_id, supplier_id, price):
    query = """
        INSERT INTO products
            (product_name, category_id, supplier_id, price)
        VALUES
            (%s, %s, %s, %s)
        RETURNING product_id;
    """

    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    query,
                    (name, category_id, supplier_id, price)
                )

                product_id = cursor.fetchone()[0]

                print(f"Product added successfully. ID: {product_id}")

    except Exception as error:
        print("Error adding product:", error)


# READ
def get_products():
    query = """
        SELECT
            p.product_id,
            p.product_name,
            c.category_name,
            s.supplier_name,
            p.price
        FROM products p
        JOIN categories c
            ON p.category_id = c.category_id
        JOIN suppliers s
            ON p.supplier_id = s.supplier_id
        ORDER BY p.product_id;
    """

    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)

                products = cursor.fetchall()

                if not products:
                    print("No products found.")
                    return

                print("\nPRODUCT LIST")
                print("-" * 80)

                for product in products:
                    print(
                        f"ID: {product[0]} | "
                        f"Name: {product[1]} | "
                        f"Category: {product[2]} | "
                        f"Supplier: {product[3]} | "
                        f"Price: ₹{product[4]}"
                    )

    except Exception as error:
        print("Error fetching products:", error)


# UPDATE
def update_product(product_id, name, category_id, supplier_id, price):
    query = """
        UPDATE products
        SET
            product_name = %s,
            category_id = %s,
            supplier_id = %s,
            price = %s
        WHERE product_id = %s;
    """

    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    query,
                    (
                        name,
                        category_id,
                        supplier_id,
                        price,
                        product_id
                    )
                )

                if cursor.rowcount == 0:
                    print("Product not found.")
                else:
                    print("Product updated successfully.")

    except Exception as error:
        print("Error updating product:", error)


# DELETE
def delete_product(product_id):
    query = """
        DELETE FROM products
        WHERE product_id = %s;
    """

    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (product_id,))

                if cursor.rowcount == 0:
                    print("Product not found.")
                else:
                    print("Product deleted successfully.")

    except Exception as error:
        print("Error deleting product:", error)