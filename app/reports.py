from db import get_connection


def total_inventory_value():
    query = """
        SELECT
            COALESCE(
                SUM(i.quantity * p.price),
                0
            )
        FROM inventory i
        JOIN products p
            ON i.product_id = p.product_id;
    """

    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)

                total = cursor.fetchone()[0]

                print("\n" + "=" * 50)
                print("          TOTAL INVENTORY VALUE")
                print("=" * 50)
                print(f"Total Inventory Value: ₹{total:,.2f}")

    except Exception as error:
        print("Error generating report:", error)


def total_sales():
    query = """
        SELECT
            COALESCE(
                SUM(quantity * unit_price),
                0
            )
        FROM sale_items;
    """

    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)

                total = cursor.fetchone()[0]

                print("\n" + "=" * 50)
                print("             TOTAL SALES")
                print("=" * 50)
                print(f"Total Sales: ₹{total:,.2f}")

    except Exception as error:
        print("Error generating report:", error)


def top_selling_products():
    query = """
        SELECT
            p.product_name,
            SUM(si.quantity) AS units_sold,
            SUM(
                si.quantity * si.unit_price
            ) AS revenue
        FROM sale_items si
        JOIN products p
            ON si.product_id = p.product_id
        GROUP BY p.product_id, p.product_name
        ORDER BY units_sold DESC;
    """

    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)

                products = cursor.fetchall()

                print("\n" + "=" * 75)
                print("              TOP SELLING PRODUCTS")
                print("=" * 75)

                if not products:
                    print("No sales data available.")
                    return

                for product in products:
                    name, units, revenue = product

                    print(
                        f"Product: {name} | "
                        f"Units Sold: {units} | "
                        f"Revenue: ₹{revenue:,.2f}"
                    )

    except Exception as error:
        print("Error generating report:", error)


def sales_by_category():
    query = """
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
        GROUP BY c.category_id, c.category_name
        ORDER BY revenue DESC;
    """

    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)

                categories = cursor.fetchall()

                print("\n" + "=" * 75)
                print("                 SALES BY CATEGORY")
                print("=" * 75)

                if not categories:
                    print("No sales data available.")
                    return

                for category in categories:
                    name, units, revenue = category

                    print(
                        f"Category: {name} | "
                        f"Units Sold: {units} | "
                        f"Revenue: ₹{revenue:,.2f}"
                    )

    except Exception as error:
        print("Error generating report:", error)


def monthly_sales():
    query = """
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
    """

    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)

                results = cursor.fetchall()

                print("\n" + "=" * 60)
                print("                 MONTHLY SALES")
                print("=" * 60)

                if not results:
                    print("No sales data available.")
                    return

                for month, revenue in results:
                    print(
                        f"Month: {month.strftime('%Y-%m')} | "
                        f"Revenue: ₹{revenue:,.2f}"
                    )

    except Exception as error:
        print("Error generating report:", error)