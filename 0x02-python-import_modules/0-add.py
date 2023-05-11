#!/usr/bin/python3

if __name__ == "__main__":
    # Import the add function from add_0 module
    from add_0 import add

    # Assign values to variables
    num1 = 1
    num2 = 2

    # Calculate the sum and print the result
    result = add(num1, num2)
    print("{} + {} = {}".format(num1, num2, result))
