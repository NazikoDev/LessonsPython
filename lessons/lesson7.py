import sqlite3      #запрос

def create_tables(conn):   #создаем таблицу
    conn.execute("""
    CREATE TABLE IF NOT EXISTS student (
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         name TEXT NOT NULL,      
         age INTEGER,    
         city TEXT
         )
    """)
    conn.commit()

def add_student(conn, name, age, city):
    conn.execute("""
    INSERT INTO student (name, age, city)
    VALUES (?,?,?)
    """, (name, age, city))
    conn.commit()

if __name__ == "__main__":
    conn = sqlite3.connect("database.db")

    create_tables(conn)

    add_student(conn, "Maksat", 19, "Bishkek")
    add_student(conn, "kai", 19, "Bishkek")
    add_student(conn, "Adil", 19, "Bishkek")
    conn.close()




