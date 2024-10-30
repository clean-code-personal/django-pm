# Product information manager

Product information application for discussion

## Existing code

This repository implements CRUD operations on product information. Read the code and the tests to see what it does.

To run the tests: `python manage.py test products`

Optionally, you may run the server: `python manage.py runserver` and use http://127.0.0.1:8000/admin/ to add products, http://127.0.0.1:8000/api/products/ do perform CRUD operations.

## Your work

You need to add Order Management as a feature - keeping records of orders and the products in them.

### Add Order and OrderItem Models

Order: Represents an individual customer order. An order has order_date and total_amount.

OrderItem: Represents each product in an order. An order item has product, quantity, and price_at_order.

### Implement an API for Order Management

Add CRUD endpoints for Order. Add nested endpoints for OrderItem within each Order.
Ensure that creating an order updates product stock levels appropriately.

### Write Unit Tests:

Test the CRUD functionality for both Order and OrderItem.
Validate that the code updates stock levels when an order is created.

## Evaluation criteria

- Maintain code conventions. See the `Code conventions` step in `django-tests.yml`.
- Organization and content of the models
- Relationship between entities
- Proof of working (via unit tests)
