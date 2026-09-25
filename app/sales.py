from db import get_connection


def create_sale(customer_id, product_id, quantity):
    if quantity <= 0:
        print("Quantity must be greater than 0.")
        return

    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:

                # 1. Check product and current stock
                cursor.execute(
                    """
                    SELECT price, quantity
                    FROM products
                    JOIN inventory
                        ON products.product_id = inventory.product_id
                    WHERE products.product_id = %s
                    FOR UPDATE;
                    """,
                    (product_id,)
                )

                product = cursor.fetchone()

                if product is None:
                    print("Product not found.")
                    return

                price, stock = product

                if stock < quantity:
                    print(
                        f"Insufficient stock. "
                        f"Available stock: {stock}"
                    )
                    return

                # 2. Create sale
                cursor.execute(
                    """
                    INSERT INTO sales (customer_id)
                    VALUES (%s)
                    RETURNING sale_id;
                    """,
                    (customer_id,)
                )

                sale_id = cursor.fetchone()[0]

                # 3. Add sale item
                cursor.execute(
                    """
                    INSERT INTO sale_items
                        (sale_id, product_id, quantity, unit_price)
                    VALUES
                        (%s, %s, %s, %s);
                    """,
                    (
                        sale_id,
                        product_id,
                        quantity,
                        price
                    )
                )

                # 4. Reduce inventory
                cursor.execute(
                    """
                    UPDATE inventory
                    SET quantity = quantity - %s
                    WHERE product_id = %s;
                    """,
                    (
                        quantity,
                        product_id
                    )
                )

                # Transaction is committed automatically
                # when the 'with' block exits successfully.

                print("\nSale created successfully!")
                print(f"Sale ID: {sale_id}")
                print(f"Product price: ₹{price}")
                print(f"Quantity: {quantity}")
                print(
                    f"Total: ₹{price * quantity}"
                )

    except Exception as error:
        print("\nSale failed.")
        print("Transaction rolled back.")
        print("Error:", error)


def view_sales():
    query = """
        SELECT
            s.sale_id,
            c.customer_name,
            s.sale_date,
            SUM(
                si.quantity * si.unit_price
            ) AS total_amount
        FROM sales s
        JOIN customers c
            ON s.customer_id = c.customer_id
        JOIN sale_items si
            ON s.sale_id = si.sale_id
        GROUP BY
            s.sale_id,
            c.customer_name,
            s.sale_date
        ORDER BY s.sale_id DESC;
    """

    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)

                sales = cursor.fetchall()

                if not sales:
                    print("\nNo sales found.")
                    return

                print("\n" + "=" * 80)
                print("                         SALES")
                print("=" * 80)

                for sale in sales:
                    sale_id, customer, date, total = sale

                    print(
                        f"Sale ID: {sale_id} | "
                        f"Customer: {customer} | "
                        f"Date: {date} | "
                        f"Total: ₹{total}"
                    )

    except Exception as error:
        print("Error fetching sales:", error)


def view_sale_details(sale_id):
    query = """
        SELECT
            s.sale_id,
            c.customer_name,
            p.product_name,
            si.quantity,
            si.unit_price,
            (si.quantity * si.unit_price) AS total
        FROM sales s
        JOIN customers c
            ON s.customer_id = c.customer_id
        JOIN sale_items si
            ON s.sale_id = si.sale_id
        JOIN products p
            ON si.product_id = p.product_id
        WHERE s.sale_id = %s;
    """

    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (sale_id,))

                details = cursor.fetchall()

                if not details:
                    print("Sale not found.")
                    return

                print("\n" + "=" * 70)
                print(f"SALE DETAILS — #{sale_id}")
                print("=" * 70)

                total_amount = 0

                for detail in details:
                    (
                        sale_id,
                        customer,
                        product,
                        quantity,
                        price,
                        total
                    ) = detail

                    print(f"Customer : {customer}")
                    print(f"Product  : {product}")
                    print(f"Quantity : {quantity}")
                    print(f"Price    : ₹{price}")
                    print(f"Subtotal : ₹{total}")
                    print("-" * 70)

                    total_amount += total

                print(f"TOTAL: ₹{total_amount}")

    except Exception as error:
        print("Error fetching sale:", error)