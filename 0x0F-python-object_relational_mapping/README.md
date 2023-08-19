# 0x0F Python Object-Relational Mapping

Welcome to the "0x0F-python-object_relational_mapping" project! This project aims to teach you how to connect Python with MySQL databases using both raw SQL queries and SQLAlchemy, an Object-Relational Mapping (ORM) library. By the end of this project, you'll gain a solid understanding of database interactions, data retrieval, and storage manipulation in a Python environment.

## Project Overview

In this project, you will explore the worlds of databases and Python by completing the following tasks:

1. Connecting to a MySQL Database using `MySQLdb`.
2. Executing SQL queries to perform actions like SELECT and INSERT.
3. Utilizing SQLAlchemy ORM to abstract SQL interactions using Python classes and objects.
4. Creating and configuring a database connection engine.
5. Mapping Python classes to MySQL tables using SQLAlchemy's declarative base.
6. Performing operations on data stored in the database using SQLAlchemy ORM.

## Getting Started

To begin working on this project, follow these steps:

1. Ensure you have a MySQL server installed with version 8.0.
2. Set up the necessary Python environment on Ubuntu 20.04 with Python 3.8.5.
3. Install required dependencies, including MySQLdb (version 2.0.x) and SQLAlchemy (version 1.4.x).
4. Clone this repository to your local machine.

## Project Structure

The project directory contains the following components:

- `0-select_states.py`: A script demonstrating how to connect to the MySQL database using `MySQLdb` and perform a basic SELECT query.
- `1-filter_states.py`: A script extending the previous example to include filtering with user-specified state names.
- `2-my_filter_states.py`: A script improving upon the previous script by protecting against SQL injection.
- `3-my_safe_filter_states.py`: A script implementing additional safety measures to prevent SQL injection.
- `4-cities_by_state.py`: A script to join two tables and retrieve data using raw SQL queries.
- `5-filter_cities.py`: A script that accepts state names and lists corresponding cities using SQLAlchemy ORM.
- `model_state.py`: A Python file containing the `State` class mapped to the `states` table using SQLAlchemy.
- `7-model_state_fetch_all.py`: A script using SQLAlchemy to fetch all `State` objects from the database.
- `8-model_state_fetch_first.py`: A script using SQLAlchemy to fetch the first `State` object from the database.
- `9-model_state_filter_a.py`: A script using SQLAlchemy to fetch all `State` objects that contain the letter 'a'.
- `10-model_state_my_get.py`: A script using SQLAlchemy to fetch a specific `State` object by its name.

## Project Notes

- The provided scripts and files demonstrate progressively more advanced usage of Python, MySQL, and SQLAlchemy.
- Refer to the resources mentioned in the project description for tutorials, documentation, and tips on SQLAlchemy usage.
- Remember to follow good coding practices, including proper documentation, adherence to PEP8 style guidelines, and meaningful variable and function names.

Feel free to explore, experiment, and learn as you progress through the project. If you encounter any issues or have questions, don't hesitate to reach out for assistance.

Happy coding!
