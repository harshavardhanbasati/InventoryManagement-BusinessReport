# Inventory Management & Business Reporting System

A Python and PostgreSQL-based inventory management system designed to manage products, suppliers, inventory, customers, sales, and business reports.

The project demonstrates practical SQL, database design, CRUD operations, joins, transactions, aggregation, indexing, and Python-PostgreSQL integration.

---

## Features

### Product Management

- Add products
- View products
- Update products
- Delete products
- Associate products with categories
- Associate products with suppliers

### Inventory Management

- View current inventory
- Add stock
- Remove stock
- Prevent negative inventory
- Detect low-stock products
- Calculate inventory value

### Sales Management

- Create sales
- Check available stock before selling
- Automatically reduce inventory after a sale
- View all sales
- View individual sale details
- Calculate sale totals

### Business Reports

- Total inventory value
- Total sales
- Top-selling products
- Sales by category
- Monthly sales
- Low-stock report

### Database Features

- Primary keys
- Foreign keys
- Unique constraints
- Check constraints
- Normalized relational database design
- SQL JOINs
- GROUP BY
- Aggregate functions
- Indexes
- Transactions
- COMMIT / ROLLBACK
- Row locking using `FOR UPDATE`

---

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| PostgreSQL | Relational database |
| Psycopg | PostgreSQL connectivity |
| python-dotenv | Environment variable management |
| SQL | Database operations |
| Git | Version control |

---

## Project Structure

```text
inventory_management/
│
├── app/
│   ├── __init__.py
│   ├── db.py
│   ├── products.py
│   ├── inventory.py
│   ├── sales.py
│   ├── reports.py
│   └── main.py
│
├── database/
│   ├── schema.sql
│   ├── seed.sql
│   └── reports.sql
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
