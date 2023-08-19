#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa that match the given state name.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <mysql username> <mysql password> <database name> <state name searched>".format(sys.argv[0]))
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=db_name,
            charset="utf8"
        )

        cursor = db.cursor()
        cursor.execute("SELECT * FROM `states` WHERE BINARY `name` = %s ORDER BY `id`", (state_name,))
        states = cursor.fetchall()

        for state in states:
            print(state)

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()
