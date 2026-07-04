# BizMetric

**A full-stack Business Management & Sales Analytics Platform built with Django, PostgreSQL, JavaScript, and Bootstrap.**

BizMetric helps small and medium-sized businesses manage daily operations from a single dashboard. It combines inventory management, sales, purchases, expenses, customer and supplier management, role-based access control, and business analytics to provide actionable insights for better decision-making.

> **Status:** Portfolio Project
> **Purpose:** Demonstrate full-stack development, database design, business logic implementation, reporting, and data visualization.

---

## 🎥 Project Demo

> **Add a short demo video or GIF here (20–60 seconds).**

Example:


```text
assets/demo.gif
```

or

```text
https://your-demo-link.com
```

---

# Dashboard Preview

> **Add your main dashboard screenshot here.**

Suggested image:

```text
assets/screenshots/dashboard.png
```

![dashboard](/assets/screenshots/dashboard.png)

The dashboard provides an overview of:

* Revenue
* Profit
* Sales
* Purchases
* Expenses
* Inventory
* Monthly trends
* Top-selling products
* Business performance

---

# Features

## Multi-Business Management

Manage multiple businesses from a single account while keeping data completely isolated.

**Features**

* Create and manage multiple businesses
* Independent inventory
* Separate reports
* Separate customers and suppliers
* Individual analytics

> 📷 Screenshot:
>
> `assets/screenshots/business-list.png`

---

## Sales Management

Create and manage customer sales efficiently.

Features include:

* Customer search
* Product search
* Quantity management
* Automatic stock updates
* Invoice generation
* Profit calculation

> 📷 Screenshot:
>
> `assets/screenshots/create-sale.png`

---

## Purchase Management

Track inventory purchases from suppliers.

Features:

* Supplier management
* Purchase history
* Cost tracking
* Inventory updates

> 📷 Screenshot:
>
> `assets/screenshots/purchases.png`

---

## Inventory Management

Keep inventory synchronized with every purchase and sale.

Includes:

* Current stock
* Stock valuation
* Product categories
* Low-stock monitoring

> 📷 Screenshot:
>
> `assets/screenshots/inventory.png`

---

## Expense Tracking

Monitor business expenses to understand profitability.

Examples:

* Rent
* Salary
* Utilities
* Marketing
* Miscellaneous expenses

> 📷 Screenshot:
>
> `assets/screenshots/expenses.png`

---

## Customer Management

Manage customer information and purchase history.

Features:

* Customer profiles
* Contact information
* Purchase history
* Outstanding balances

> 📷 Screenshot:
>
> `assets/screenshots/customers.png`

---

## Supplier Management

Maintain supplier records and purchasing history.

Features:

* Supplier details
* Contact information
* Purchase records

> 📷 Screenshot:
>
> `assets/screenshots/suppliers.png`

---

## Reports & Analytics

Generate business insights using interactive dashboards.

Reports include:

* Revenue trends
* Profit analysis
* Monthly sales
* Expense reports
* Product performance
* Customer analytics

> 📷 Screenshot:
>
> `assets/screenshots/reports.png`

---

## Role-Based Access Control

Secure access using custom roles and permissions.

Examples:

* Owner
* Manager
* Employee

Features:

* Authentication
* Authorization
* Protected views
* Permission-based navigation

> 📷 Screenshot:
>
> `assets/screenshots/users-permissions.png`

---

# Technology Stack

### Backend

* Django
* Django ORM
* PostgreSQL

### Frontend

* HTML
* CSS
* Bootstrap
* JavaScript

### Database

* PostgreSQL (Supabase)

### Deployment

* Render
* Supabase

### Tools

* Git
* GitHub
* VS Code

---

# Project Architecture

```text
Browser
      │
      ▼
Bootstrap + JavaScript
      │
      ▼
Django Views
      │
      ▼
Business Logic
      │
      ▼
Django ORM
      │
      ▼
PostgreSQL (Supabase)
```

---

# Key Backend Highlights

This project focuses heavily on backend development and business logic.

Highlights include:

* Django ORM optimization
* Model relationships
* Foreign keys
* Transactions
* Aggregations
* Permission decorators
* Class-based views
* Authentication
* Custom management commands
* Data seeding
* Dynamic dashboard APIs

---

# Business Modules

* Dashboard
* Sales
* Purchases
* Inventory
* Customers
* Suppliers
* Expenses
* Reports
* User Management
* Authentication

---

# Database Design

The application uses a relational database with interconnected models including:

* Business
* User
* Customer
* Supplier
* Product
* Category
* Sale
* Sale Item
* Purchase
* Purchase Item
* Expense

> 📷 Optional:
>
> Add an ER Diagram here.
>
> `assets/screenshots/database-diagram.png`

---

# Performance Considerations

Implemented optimizations include:

* Database aggregations
* Efficient ORM queries
* Filtered reports
* Dynamic dashboard loading
* Optimized static assets
* WhiteNoise static file serving

---

# Security

* CSRF Protection
* Authentication
* Authorization
* Role-based permissions
* Server-side validation
* Protected business data

---

# Installation

Clone the repository:

```bash
git clone https://github.com/your-username/django-sales-analytics.git
```

Navigate to the project:

```bash
cd django-sales-analytics
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Create a superuser:

```bash
python manage.py createsuperuser
```

Start the server:

```bash
python manage.py runserver
```

---

# Screenshots

Create this folder structure:

```text
assets/
└── screenshots/
    ├── dashboard.png
    ├── create-sale.png
    ├── inventory.png
    ├── purchases.png
    ├── expenses.png
    ├── reports.png
    ├── customers.png
    ├── suppliers.png
    ├── users-permissions.png
    ├── business-list.png
    └── database-diagram.png
```

---

# Future Improvements

* Barcode scanning
* Invoice PDF generation
* Email notifications
* GST reports
* Advanced forecasting
* Export to Excel/PDF
* Mobile-responsive enhancements
* REST API expansion

---

# What This Project Demonstrates

* Full-stack web development
* Django architecture
* PostgreSQL database design
* Business workflow implementation
* Dashboard development
* Data visualization
* Authentication & authorization
* CRUD operations
* Reporting & analytics
* Production deployment

---

# Author

**Abhishek Chaudhary**

If you found this project interesting, feel free to explore the codebase or connect with me.
