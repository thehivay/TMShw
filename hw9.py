import sqlite3


def task_1(db1):
    conn = sqlite3.connect(db1)
    curs = conn.cursor()
    curs.execute("CREATE TABLE Shops("
                 "id int NOT NULL PRIMARY KEY,"
                 "name varchar(32) NOT NULL,"
                 "address varchar(32),"
                 "staff_amount int NOT NULL)")
    curs.execute("CREATE TABLE Departments("
                 "id int NOT NULL PRIMARY KEY,"
                 "sphere varchar(32) NOT NULL,"
                 "staff_amount int NOT NULL,"
                 "shop int NOT NULL,"
                 "FOREIGN KEY (shop) REFERENCES Shops(id))")
    curs.execute("CREATE TABLE Items("
                 "id int NOT NULL PRIMARY KEY,"
                 "name varchar(32) NOT NULL,"
                 "description text,"
                 "price int NOT NULL,"
                 "department int NOT NULL,"
                 "FOREIGN KEY (department) REFERENCES Departments(id))")
    conn.commit()
    pass

# task9_2


def task_2(db1):
    conn = sqlite3.connect(db1)
    curs = conn.cursor()

    data = [(1, 'Auchan', None, 250),
            (2, 'IKEA', 'Street Žirnių g. 56, Vilnius, Lithuania.', 500)]
    curs.executemany("INSERT INTO Shops VALUES (?,?,?,?)", data)

    data = [(1, 'Furniture', 250, 1),
            (2, 'Furniture', 300, 2),
            (3, 'Dishes', 200, 2)]
    curs.executemany("INSERT INTO Departments VALUES (?,?,?,?)", data)

    data = [(1, 'Table', 'Cheap wooden table', 300, 1),
            (2, 'Table', None, 750, 2),
            (3, 'Bed', 'Amazing wooden bed', 1200,2),
            (4, 'Cup', None, 10, 3),
            (5, 'Plate', 'Glass plate', 20, 3)]
    curs.executemany("INSERT INTO Items VALUES (?,?,?,?,?)", data)

    conn.commit()
    pass

# task9_3


def task_3(db1):
    t = []
    conn = sqlite3.connect(db1)
    curs = conn.cursor()

    # a
    curs.execute("SELECT * FROM Items WHERE description NOT NULL")
    t.append(curs.fetchall())

    # b
    curs.execute("SELECT DISTINCT sphere FROM Departments WHERE staff_amount > 200")
    t.append(curs.fetchall())

    # c
    curs.execute("SELECT address FROM Shops WHERE address LIKE 'i%'")
    t.append(curs.fetchall())

    # d
    curs.execute("SELECT Items.name FROM Items, Departments "
                 "WHERE Items.department = Departments.id AND Departments.sphere = 'Furniture'")
    t.append(curs.fetchall())

    # e
    curs.execute("SELECT DISTINCT Shops.name FROM Items, Departments, Shops "
                 "WHERE Items.department = Departments.id AND Departments.shop = Shops.id "
                 "AND Items.description NOT NULL")
    t.append(curs.fetchall())

    # f
    curs.execute("SELECT Items.name, Items.description, Items.price, "
                 "'department_{sphere}' || Departments.sphere, "
                 "'department_{staff_amount}' || Departments.staff_amount, "
                 "'shop_{name}' || Shops.name, "
                 "'shop_{address}' || Shops.address, "
                 "'shop_{staff_amount}' || Shops.staff_amount "
                 "FROM Items JOIN Departments "
                 "ON Items.department = Departments.id "
                 "JOIN Shops ON Departments.shop = Shops.id")
    t.append(curs.fetchall())

    return tuple(t)


p = 'base.db'
task_1(p)
task_2(p)
print('--------------', '\n', task_3(p))
task_4(p)
task_5(p)
