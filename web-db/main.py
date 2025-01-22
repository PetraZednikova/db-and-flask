import sqlite3

conn = sqlite3.connect("my_db.db")

cur = conn.cursor()

cur.execute("""
""")

data = cur.fetchall()

conn.close()
