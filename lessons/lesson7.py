import sqlite3      #запрос

def create_tables():   #создаем таблицу
    connetion.execute("""
    CREATE TABLE students (
         name TEXT,      #назввание колонки (name)  NOT NULL(ограничение нельзя оставлять не заполненой)
         age INTEGER,    #INTEGER,(только цифры)
         city TEXT,
         )
         """)

if __name__ == "__main__":
    connetion = sqlite3.connect("database.db")
    create_tables()


