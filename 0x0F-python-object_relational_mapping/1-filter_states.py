#!/usr/bin/python3
# Lists all states with a name starting with N from the database hbtn_0e_0_usa.
# Usage: ./1-filter_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>
import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to the MySQL database using provided credentials
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    
    # Execute SQL query to select states starting with N
    c.execute("SELECT * FROM `states` WHERE `name` LIKE 'N%' ORDER BY `id`")
    
    # Fetch and print states that meet the condition
    [print(state) for state in c.fetchall()]
    
    # Close cursor and database connection
    c.close()
    db.close()
