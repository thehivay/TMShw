import sqlite3


def task10_1(db1):
    conn = sqlite3.connect(db1)
    curs = conn.cursor()
    curs.execute("UPDATE Items SET price = price + 100 WHERE name LIKE 'B%' OR name LIKE '%e'")
    conn.commit()
    pass


p = 'base.db'
task10_1(p)
