from product import (
    add_product,
    get_products,
    update_product,
    delete_product
)

from inventory import (
    view_inventory,
    stock_in,
    stock_out,
    low_stock_report
)

from sales import (
    create_sale,
    view_sales,
    view_sale_details
)

from reports import (
    total_inventory_value,
    total_sales,
    top_selling_products,
    sales_by_category,
    monthly_sales
)


def pause():
    input("\nPress Enter to continue...")


# =========================
# PRODUCT MANAGEMENT
# =========================

def add_product_menu():
    try:
        name = input("Product name: ").strip()
        category_id = int(input("Category ID: "))
        supplier_id = int(input("Supplier ID: "))
        price = float(input("Price: "))

        if not name:
            print("Product name cannot be empty.")
            return

        if price < 0:
            print("Price cannot be negative.")
            return

        add_product(
            name,
            category_id,
            supplier_id,
            price
        )

    except ValueError:
        print("Please enter valid values.")


def update_product_menu():
    try:
        product_id = int(input("Product ID: "))
        name = input("New product name: ").strip()
        category_id = int(input("New category ID: "))
        supplier_id = int(input("New supplier ID: "))
        price = float(input("New price: "))

        if not name:
            print("Product name cannot be empty.")
            return

        if price < 0:
            print("Price cannot be negative.")
            return

        update_product(
            product_id,
            name,
            category_id,
            supplier_id,
            price
        )

    except ValueError:
        print("Please enter valid values.")


def delete_product_menu():
    try:
        product_id = int(input("Product ID: "))

        confirmation = input(
            "Are you sure you want to delete this product? (y/n): "
        ).strip().lower()

        if confirmation == "y":
            delete_product(product_id)
        else:
            print("Delete cancelled.")

    except ValueError:
        print("Product ID must be a number.")


def product_menu():
    while True:
        print("\n" + "=" * 45)
        print("          PRODUCT MANAGEMENT")
        print("=" * 45)

        print("1. Add Product")
        print("2. View Products")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Back")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_product_menu()

        elif choice == "2":
            get_products()

        elif choice == "3":
            update_product_menu()

        elif choice == "4":
            delete_product_menu()

        elif choice == "5":
            break

        else:
            print("Invalid choice.")


# =========================
# INVENTORY MANAGEMENT
# =========================

def inventory_menu():
    while True:
        print("\n" + "=" * 45)
        print("          INVENTORY MANAGEMENT")
        print("=" * 45)

        print("1. View Inventory")
        print("2. Stock In")
        print("3. Stock Out")
        print("4. Low Stock Report")
        print("5. Back")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            view_inventory()

        elif choice == "2":
            try:
                product_id = int(input("Product ID: "))
                quantity = int(input("Quantity to add: "))

                stock_in(product_id, quantity)

            except ValueError:
                print("Please enter valid numbers.")

        elif choice == "3":
            try:
                product_id = int(input("Product ID: "))
                quantity = int(input("Quantity to remove: "))

                stock_out(product_id, quantity)

            except ValueError:
                print("Please enter valid numbers.")

        elif choice == "4":
            try:
                threshold_input = input(
                    "Low-stock threshold [10]: "
                ).strip()

                threshold = (
                    int(threshold_input)
                    if threshold_input
                    else 10
                )

                low_stock_report(threshold)

            except ValueError:
                print("Threshold must be a number.")

        elif choice == "5":
            break

        else:
            print("Invalid choice.")


# =========================
# SALES MANAGEMENT
# =========================

def create_sale_menu():
    try:
        customer_id = int(input("Customer ID: "))
        product_id = int(input("Product ID: "))
        quantity = int(input("Quantity: "))

        create_sale(
            customer_id,
            product_id,
            quantity
        )

    except ValueError:
        print("Please enter valid numbers.")


def sale_details_menu():
    try:
        sale_id = int(input("Sale ID: "))

        view_sale_details(sale_id)

    except ValueError:
        print("Sale ID must be a number.")


def sales_menu():
    while True:
        print("\n" + "=" * 45)
        print("            SALES MANAGEMENT")
        print("=" * 45)

        print("1. Create Sale")
        print("2. View Sales")
        print("3. View Sale Details")
        print("4. Back")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            create_sale_menu()

        elif choice == "2":
            view_sales()

        elif choice == "3":
            sale_details_menu()

        elif choice == "4":
            break

        else:
            print("Invalid choice.")


# =========================
# REPORTS
# =========================

def reports_menu():
    while True:
        print("\n" + "=" * 45)
        print("             BUSINESS REPORTS")
        print("=" * 45)

        print("1. Total Inventory Value")
        print("2. Total Sales")
        print("3. Top Selling Products")
        print("4. Sales by Category")
        print("5. Monthly Sales")
        print("6. Back")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            total_inventory_value()

        elif choice == "2":
            total_sales()

        elif choice == "3":
            top_selling_products()

        elif choice == "4":
            sales_by_category()

        elif choice == "5":
            monthly_sales()

        elif choice == "6":
            break

        else:
            print("Invalid choice.")


# =========================
# MAIN MENU
# =========================

def main():
    while True:
        print("\n")
        print("=" * 50)
        print("       INVENTORY MANAGEMENT SYSTEM")
        print("=" * 50)

        print("1. Product Management")
        print("2. Inventory Management")
        print("3. Sales Management")
        print("4. Business Reports")
        print("5. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            product_menu()

        elif choice == "2":
            inventory_menu()

        elif choice == "3":
            sales_menu()

        elif choice == "4":
            reports_menu()

        elif choice == "5":
            print("\nThank you for using Inventory Management System.")
            break

        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()