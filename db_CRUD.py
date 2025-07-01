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
