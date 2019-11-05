#! src/bin/python3
# -*- coding: utf-8 -*-
import sqlite3


def load_data(conn, data):

    try:
        cur = conn.cursor()
        cur.execute('SELECT SQLITE_VERSION()')
        v = cur.fetchone()[0]
        print("SQLite version: {}".format(v))

        cur.execute("CREATE TABLE person(id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, age INTEGER)")
        cur.execute("CREATE TABLE pet(id INTEGER PRIMARY KEY, name TEXT, breed TEXT, age INTEGER, dead INTEGER)")
        cur.execute("CREATE TABLE person_pet(person_id INTEGER, pet_id INTEGER)")

        # Execute insert statements
        for schema, values in data.items():

            if schema == "Person":
                sql = "INSERT INTO person VALUES (?, ?, ?, ?)"
                cur.executemany(sql, values)
            elif schema == "Pet":
                sql = "INSERT INTO pet VALUES (?, ?, ?, ?, ?)"
                cur.executemany(sql, values)
            else:
                sql = "INSERT INTO person_pet VALUES (?, ?)"
                cur.executemany(sql, values)
        conn.commit()
        # Test query
        cur.execute("SELECT * from person")
        d = cur.fetchall()
        for row in d:
            print(row)

    except sqlite3.Error as error:
        print("Failed to load data. Error: {}".format(error))

# 2 What is the purpose of the person_pet table?
# To connect/join person table with pet table


def get_data():

    d = {
        "Person": [(1, 'James', 'Smith', 41),
                   (2, 'Diana', 'Greene', 23),
                   (3, 'Sara', 'White', 27),
                   (4, 'William', 'Gibson', 23)],
        "Pet": [(1, 'Rusty', 'Dalmation', 4, 1),
                (2, 'Bella', 'AlaskanMalamute', 3, 0),
                (3, 'Max', 'CockerSpaniel', 1, 0),
                (4, 'Rocky', 'Beagle', 7, 0),
                (5, 'Rufus', 'CockerSpaniel', 1, 0),
                (6, 'Spot', 'Bloodhound', 2, 1)],
        "Person_Pet": [(1, 1),
                       (1, 2),
                       (2, 3),
                       (2, 4),
                       (3, 5),
                       (4, 6)]
    }

    return d


if __name__ == '__main__':

    conn = None
    try:
        conn = sqlite3.connect('pets.db')

    except sqlite3.Error as error:
        print("Failed to establish database connection. Error: {}".format(error))

    values = get_data()
    load_data(conn, values)

    if conn:
        conn.close()
