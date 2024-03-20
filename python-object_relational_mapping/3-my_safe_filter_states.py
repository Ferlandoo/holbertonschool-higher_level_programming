#!/usr/bin/python3
"""Takes in an argument and displays values in the states table of
hbtn_0e_0_usa where name matches the argument."""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    u = argv[1]
    p = argv[2]
    d = argv[3]
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=u,
        passwd=p,
        db=d,
        charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY %s", (argv[4], ))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
