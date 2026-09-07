import sqlite3


DATABASE_NAME = "expenses.db"


def create_database():
    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            category TEXT NOT NULL,
            description TEXT NOT NULL,
            amount REAL NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def add_expense(date, category, description, amount):
    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO expenses (date, category, description, amount)
        VALUES (?, ?, ?, ?)
    """, (date, category, description, amount))

    connection.commit()
    connection.close()


def get_all_expenses():
    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM expenses
        ORDER BY date DESC
    """)

    expenses = cursor.fetchall()

    connection.close()

    return expenses


def delete_expense(expense_id):
    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM expenses
        WHERE id = ?
    """, (expense_id,))

    connection.commit()

    deleted_rows = cursor.rowcount

    connection.close()

    return deleted_rows
def update_expense(expense_id, date, category, description, amount):
    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        UPDATE expenses
        SET date = ?,
            category = ?,
            description = ?,
            amount = ?
        WHERE id = ?
    """, (date, category, description, amount, expense_id))

    connection.commit()

    updated_rows = cursor.rowcount

    connection.close()

    return updated_rows

def get_monthly_total(year, month):
    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    month_string = f"{year:04d}-{month:02d}"

    cursor.execute("""
        SELECT COALESCE(SUM(amount), 0)
        FROM expenses
        WHERE date LIKE ?
    """, (month_string + "%",))

    total = cursor.fetchone()[0]

    connection.close()

    return total