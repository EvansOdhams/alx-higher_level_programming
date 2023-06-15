# 0x0C. Python - Almost a circle
This project is part of the AirBnB curriculum, focusing on reviewing various Python concepts and features. The goal is to implement classes and methods related to shapes, specifically rectangles and squares, while also covering topics such as serialization, deserialization, JSON handling, and unit testing.

## Table of Contents
# Requirements
Project Structure
Usage
Testing
Author

#Requirements
Python 3.8.5
pycodestyle 2.8.*
unittest module
Project Structure
The project structure is organized as follows:

csharp
Copy code
# 0x0C-python-almost_a_circle/
├── models/
│   ├── base.py
│   ├── rectangle.py
│   └── square.py
├── tests/
│   ├── test_models/
│   │   ├── test_base.py
│   │   ├── test_rectangle.py
│   │   └── test_square.py
│   └── test_utils.py
└── README.md
The models directory contains the Python modules for the base, rectangle, and square classes.
The tests directory contains the test files corresponding to each module and additional utility tests.
The README.md file provides an overview of the project and instructions for usage and testing.
Usage
To use the classes and methods implemented in this project, follow these steps:


#Clone the repository:
bash
Copy code
git clone https://github.com/evansodhams/alx-higher_level_programming.git
Change into the project directory:
bash
Copy code
cd alx-higher_level_programming/0x0C-python-almost_a_circle
You can now import the classes in your Python scripts by using the following import statements:
python
Copy code
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
Start using the classes and their methods based on your requirements.

##Testing
The project includes unit tests for all implemented classes and methods. To run the tests, follow these steps:

Ensure you are in the project directory:
bash
Copy code
cd alx-higher_level_programming/0x0C-python-almost_a_circle

## Run the tests using the following command:
bash
Copy code
python3 -m unittest discover tests
This command will automatically discover and run all the test files in the tests directory.
Review the test results and ensure that all tests pass successfully.
## Author
Created by Evance Odhiambo
