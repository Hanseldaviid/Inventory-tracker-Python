# Inventory-tracker-Python

# 🛒 Smart POS & Inventory Management System CLI

A Python console application simulating a Point of Sale (POS) and inventory control system. The application handles multi-item shopping sessions, dynamically tracks remaining store stock, calculates total costs, and enforces strict input validation.

## 🚀 Features

* **Dynamic Stock Tracking:** Displays remaining inventory levels in real-time before each product selection.
* **Stock Limit Enforcement:** Prevents over-purchasing by validating customer requests against available store inventory.
* **Interactive Menu System:** Powered by Python's `match-case` statement for clean, structured navigation.
* **Unified Error Handling:** Wrapped in a single top-level `try-except` block to gracefully capture invalid data types (`ValueError`) across all user prompts.
* **Data Accumulation:** Tracks both total items purchased and cumulative session cost across multiple distinct products.
* **Checkout Summary:** Outputs an itemized final breakdown of purchased goods, total payment due, and updated inventory levels.

## 🛠️ Concepts Applied

* **State Management:** Decrementing stock levels and updating persistent variables (`+=`, `-=`).
* **Nested Control Flow:** Combining `for` loops (item counter) with `while True` loops (input validation).
* **Selection Logic:** `match-case` statements combined with multi-branch `if-elif-else` conditionals.
* **Robust Exception Handling:** Protecting user input steps with `try-except`.
