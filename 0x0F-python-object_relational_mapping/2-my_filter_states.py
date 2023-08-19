#!/usr/bin/python3
# Displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
import sys
import MySQLdb

if __name__ == "__main__":
    # Arguments: mysql username, mysql password, database name, and state name searched
    if len(sys.argv) != 5:
        print("Usage: {} <mysql username> <mysql password> <database name> <state name searched>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(user=username, passwd=password, db=database)
    c = db.cursor()
    
    # Use format to create the SQL query with the user input
    query = "SELECT * FROM `states` WHERE `name` = '{}' ORDER BY `id`".format(state_name)
    c.execute(query)
    
    # Display results
    [print(state) for state in c.fetchall()]
    
    # Close cursor and database connection
    c.close()
    db.close()
