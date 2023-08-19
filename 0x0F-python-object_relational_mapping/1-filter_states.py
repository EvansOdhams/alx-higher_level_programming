#!/usr/bin/python3
import MySQLdb

def filter_states(username, password, database):
  """
  Filters states from the database hbtn_0e_0_usa.

  Args:
    username: The MySQL username.
    password: The MySQL password.
    database: The MySQL database name.

  Returns:
    A list of states with a name starting with N (upper N).
  """

  connection = MySQLdb.connect(host="localhost", user=username, password=password, db=database)
  cursor = connection.cursor()

  query = "SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
  cursor.execute(query)

  states = []
  for row in cursor:
    states.append((row[0], row[1]))

  connection.close()

  return states

if __name__ == "__main__":
  username = input("Enter MySQL username: ")
  password = input("Enter MySQL password: ")
  database = input("Enter MySQL database name: ")

  states = filter_states(username, password, database)

  for state in states:
    print(state)
