#!/usr/bin/python3
"""
Lists all states with a name starting with N from the database hbtn_0e_0_usa.
Usage: ./1-filter_states.py <mysql username> \
                            <mysql password> \
                            <database name>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Check if all arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    # Connect to MySQL server
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    # Create a cursor object to interact with the database
    c = db.cursor()

    # Execute the SQL query to retrieve and filter states
    c.execute("SELECT * FROM `states` WHERE `name` LIKE 'N%' ORDER BY `id`")

    # Print the results
    [print(state) for state in c.fetchall()]

    # Clean up
    c.close()
    db.close()
