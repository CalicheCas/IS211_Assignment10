#! src/bin/python3
# -*- coding: utf-8 -*-
import sqlite3


def query_engine(con):

    with con:

        while True:
            entry = int(input("Please enter a person ID: "))

            if entry == -1:
                break

            cur = con.cursor()
            cur.execute("SELECT * FROM person WHERE id=:id", {"id": entry})

            data = cur.fetchone()

            # If user is found
            if data != None:

                fn = data[1]
                ln = data[2]
                age = data[3]
                print("{} {}, {} years old".format(fn, ln, age))
                cur.execute("SELECT pet_id FROM person_pet WHERE person_id=:id", {"id": entry})
                vals = cur.fetchall()

                for p in vals:

                    pet_id = p[0]
                    cur.execute("SELECT * FROM pet WHERE id=:id", {"id": pet_id})
                    pet = cur.fetchone()
                    pname = pet[1]
                    breed = pet[2]
                    page = pet[3]
                    dead = pet[4]

                    if dead == 1:
                        print("{} {} owned {}, a {} that was {} years old.".format(fn, ln, pname, breed, page))
                    else:
                        print("{} {} owns {}, a {} that is {} years old.".format(fn, ln, pname, breed, page))
            else:
                print("Error, person not found")


if __name__ == '__main__':

    conn = None
    try:
        conn = sqlite3.connect('pets.db')

    except sqlite3.Error as error:
        print("Failed to establish database connection. Error: {}".format(error))

    query_engine(conn)

    if conn:
        conn.close()
