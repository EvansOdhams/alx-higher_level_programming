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
    # Check for the correct number of command-line arguments
    if len(sys.argv) != 4:
        print("Usage: ./1-filter_states.py <mysql username> <mysql password> <database name>")
        sys.exit(1)
    
    # Retrieve command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    
    try:
        # Connect to the MySQL server using a UNIX socket
        db = MySQLdb.connect(user=username, passwd=password, db=db_name, unix_socket="/var/run/mysqld/mysqld.sock")
        c = db.cursor()

        # Execute the query to retrieve states starting with 'N'
        query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id"
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
