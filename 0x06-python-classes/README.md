# 0x06-python-classes

## Overview

In this project I revisit object-oriented programming (OOP) concepts but in Python not JAVA.

## Table of Contents

- [Scripts](#scripts)
- [Requirements](#requirements)
- [Installation](#installation)
- [Author](#author)

## Scripts

* **0. My first square**
  * [0-square.py](./0-square.py): A class `Square` that defines a square.

* **1. Square with size**
  * [1-square.py](./1-square.py): A class `Square` that defines a square, with Private instance attribute `size` and Instantiation with `size`.

* **2. Size validation**
  * [2-square.py](./2-square.py): A class `Square` that defines a square, with Instantiation with optional `size`.

* **3. Area of a square**
  * [3-square.py](./3-square.py): A class `Square` that defines a square, with Public instance attribute `def area(self):` that returns the current square area.

* **4. Access and update private attribute**
  * [4-square.py](./4-square.py): A lass `Square` that defines a square, with Property `def size(self):` to retrieve the private instance  attribute `self` and Property setter `def size(self, value):` to set `self`.

* **5. Printing a square**
  * [5-square.py](./5-square.py): A class `Square` that defines a square, with Public instance method `def my_print(self):` that prints the square with the character `#` to standard output (if `size` == 0 -> prints an empty line).

* **6. Coordinates of a square**
  * [6-square.py](./6-square.py): A class `Square` that defines a square with public and private attributes with Private instance attribute `position`, Property `def position(self):` to retreive `position, Property setter `def position(self, value):` to set `position and Instantiation with optional `size` and `position`:  `def __init__(self, size=0, position=(0, 0)).

* **7. Singly linked list**
  * [100-singly_linked_list.py](./100-singly_linked_list.py): Python classes `Node` and `SinglyLinkedList` that define a node of a singly-linked.

* **8. Print Square instance**
  * [101-square.py](./101-square.py): A class `Square` that defines a square and sets printing of a `Square` instance equivalent to  `my_print()`.

* **9. Compare 2 squares**
  * [102-square.py](./102-square.py): A class `Square` that defines a square. and enables `Square` instance to answer to comparators: ==, !=, >, >=, < and <= based on the square area.

* **10. ByteCode -> Python #5**
  * [103-magic_class.py](./103-magic_class.py): A function that gives provided bytecode.

## Requirements

- Python 3.8.5
- pycodestyle 2.8.*

## Installation

Clone the repository to your local machine:

   ```bash
   git clone https://github.com/ipfanimuleya/alx-higher_level_programming.git


## Author

[Ipfani Muleya](https://github.com/IpfaniMuleya)
