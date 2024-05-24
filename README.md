# Orders Management System

This repository contains a simple Python script for managing food orders. The script allows users to place orders for different menu items, keeps track of the total bill, and provides functionality to reset the orders.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Classes](#classes)
- [Functions](#functions)
- [Example](#example)
- [Contributing](#contributing)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/orders-management-system.git
    ```
2. Navigate to the project directory:
    ```bash
    cd orders-management-system
    ```
3. Make sure you have Python installed (the script is compatible with Python 3.x).

## Usage

To run the script, execute the following command in your terminal:
```bash
python orders.py
```

Follow the prompts to place orders, reset the menu, and view the current bill.

## Classes

### `Orders`

This class represents a menu item and its associated attributes.

#### Attributes:
- `item` (str): The name of the item.
- `price` (int): The price of the item.
- `desc` (str): A description of the item.
- `orders` (int): The number of orders for this item.
- `code` (int): A unique code for the item.

#### Methods:
- `pm(self)`: Prints the details of the item.

## Functions

### `reset()`

Resets the order count for all menu items and the total bill.

### `pmenu()`

Prints the menu and prompts the user to enter a food code to order.

### `po()`

Prints the orders placed so far and the total bill.

## Example

Upon running the script, the user will be prompted with the menu:

```
code: 1 
Pizza  Rs.200   Description: Italian

code: 2 
Burger  Rs.100   Description: American

code: 3 
Dosa  Rs.80   Description: Indian

Enter code 0 to reset
Enter food code: 
```

Users can enter the food code and quantity to place orders. To reset the orders, enter code `0`.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---
