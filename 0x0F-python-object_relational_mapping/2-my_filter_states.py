#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
Usage: ./2-my_filter_states.py <mysql username> \
                               <mysql password> \
                               <database name> \
                               <state name searched>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Check for the correct number of command-line arguments
    if len(sys.argv) != 5:
        print("Usage: ./2-my_filter_states.py <mysql username> <mysql password> <database name> <state name searched>")
        sys.exit(1)
    
    # Retrieve command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    
    try:
        # Connect to the MySQL server using a UNIX socket
        db = MySQLdb.connect(user=username, passwd=password, db=db_name, unix_socket="/var/run/mysqld/mysqld.sock")
        c = db.cursor()

        # Create the SQL query using format and user input
        query = "SELECT * FROM states WHERE name = '{}' ORDER BY id".format(state_name)
        c.execute(query)

        # Fetch and print the results
        results = c.fetchall()
        for result in results:
            print(result)

        # Close the cursor and the connection
        c.close()
        db.close()
    
    except MySQLdb.Error as e:
        print("MySQL Error:", e)
        sys.exit(1)
