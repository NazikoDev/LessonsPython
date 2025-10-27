import sqlite3

def create_tables(conn):
    conn.execute("DROP TABLE IF EXISTS books")
    conn.execute("""
    CREATE TABLE IF NOT EXISTS books(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    autor TEXT,
    publication_year INTEGER,
    genre TEXT,
    number_of_pages TEXT,
    number_of_copies TEXT
    )
    """)

def add_book(conn, name, autor, publication_year, genre, number_of_pages, number_of_copies):
    conn.execute("""
    INSERT INTO books(name, autor, publication_year, genre, number_of_pages, number_of_copies)
    VALUES(?,?,?,?,?,?)
    """, (name, autor, publication_year, genre, number_of_pages, number_of_copies))
    conn.commit()

def delete_books(conn, book_id):
    conn.execute("""
    DELETE FROM books WHERE id = ?;""", (book_id,))
    conn.commit()
    print(f"Книга с id={book_id} удалена.")

def get_all_book(conn):
    result = conn.execute("""
    SELECT * FROM books
    WHERE """)
if __name__ == "__main__":
    conn = sqlite3.connect("books.db")

    create_tables(conn)

    add_book(conn, "Маленький принц", "Антуан", 1943, "сказка", 100, 200)
    add_book(conn, "Алиса в стране чудес", "Льюис", 1865, "сказка", 150, 100)
    add_book(conn, "Денискины рассказы", "Виктор", 1959, "юмор рассказы", 200, 5)
    # delete_book(conn,3
    conn.close()





