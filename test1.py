import sqlite3
conn=sqlite3.connect("test.db")
cursor=conn.cursor()
cursor.execute("""
    create table people(
    id int primary key,
    name text not null,
    age int
    )
""")
conn.commit()
cursor.close()
conn.close()