import mysql.connector

DB_CONFIG = {
    'host':'localhost',
    'port': 3306,
    'user':'root',
    'password':"Buzils75!",
    'database':'library'
}
headers = ['id', 'name', 'surname']
def get_conn():
    return mysql.connector.connect(**DB_CONFIG)

def load_authors():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("select * from authors")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    authors =[]
    for row in rows:
        author = {}
        for i in range(len(headers)):
            author[headers[i]] = str(row[i])
        authors.append(author)
    return authors

def add_author(authors):
    print("Adding author:")
    print("Add name:")
    name = input()
    print("Add surname:")
    surname = input()

    conn = get_conn()
    cur = conn.cursor()

    cur.execute("INSERT INTO authors(name, surname) VALUES (%s, %s)",
                (name, surname))
    conn.commit()

    cur.close()
    conn.close()

def correct_author(authors):
    print("Select ID to be corrected.")
    id = input()
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("select * from authors WHERE id = %s",(id,))
    row = cur.fetchone()
    if row:
        print(f"{row[0]}. author {row[1]} {row[2]}")
        print("enter name")
        name = input()
        print("enter surname")
        surname = input()
        cur.execute(
            "UPDATE authors SET name = %s, surname = %s WHERE id = %s;",
            (name, surname, id)
        )
        conn.commit()
    cur.close()
    conn.close()


def delete_author(authors):
    print("Select ID to be deleted: ")
    id = input()

    conn = get_conn()
    cur = conn.cursor()

    cur.execute("DELETE FROM authors WHERE id = %s", (id,))
    conn.commit()

    cur.close()
    conn.close()
    print("deleted")



