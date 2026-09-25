from db import get_connection


def view_inventory():
    query = """
        SELECT
            i.product_id,
            p.product_name,
            i.quantity,
            p.price,
            (i.quantity * p.price) AS inventory_value
        FROM inventory i
        JOIN products p
            ON i.product_id = p.product_id
        ORDER BY i.product_id;
    """

    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                inventory = cursor.fetchall()

                if not inventory:
                    print("\nNo inventory records found.")
                    return

                print("\n" + "=" * 85)
                print("                         INVENTORY")
                print("=" * 85)

                for item in inventory:
                    product_id, name, quantity, price, value = item

                    print(
                        f"ID: {product_id} | "
                        f"Product: {name} | "
                        f"Stock: {quantity} | "
                        f"Price: ₹{price} | "
                        f"Value: ₹{value}"
                    )

    except Exception as error:
        print("Error fetching inventory:", error)


def stock_in(product_id, quantity):
    if quantity <= 0:
        print("Quantity must be greater than 0.")
        return

    query = """
        UPDATE inventory
        SET quantity = quantity + %s
        WHERE product_id = %s;
    """

    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    query,
                    (quantity, product_id)
                )

                if cursor.rowcount == 0:
                    print("Product not found in inventory.")
                else:
                    print(
                        f"{quantity} units added successfully."
                    )

    except Exception as error:
        print("Error adding stock:", error)


def stock_out(product_id, quantity):
    if quantity <= 0:
        print("Quantity must be greater than 0.")
        return

    query = """
        UPDATE inventory
        SET quantity = quantity - %s
        WHERE product_id = %s
        AND quantity >= %s;
    """

    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    query,
                    (quantity, product_id, quantity)
                )

                if cursor.rowcount == 0:
                    print(
                        "Insufficient stock or product not found."
                    )
                else:
                    print(
                        f"{quantity} units removed successfully."
                    )

    except Exception as error:
        print("Error removing stock:", error)


def low_stock_report(threshold=10):
    query = """
        SELECT
            i.product_id,
            p.product_name,
            i.quantity
        FROM inventory i
        JOIN products p
            ON i.product_id = p.product_id
        WHERE i.quantity <= %s
        ORDER BY i.quantity ASC;
    """

    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (threshold,))
                products = cursor.fetchall()

                print("\n" + "=" * 55)
                print("                  LOW STOCK REPORT")
                print("=" * 55)

                if not products:
                    print("No low-stock products.")
                    return

                for product in products:
                    print(
                        f"ID: {product[0]} | "
                        f"Product: {product[1]} | "
                        f"Stock: {product[2]}"
                    )

    except Exception as error:
        print("Error generating low-stock report:", error)