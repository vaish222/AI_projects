import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
connection = sqlite3.connect("student_grades.db")
cursor = connection.cursor()

# Create a table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS grades (
        id INTEGER PRIMARY KEY,
        name TEXT,
        subject TEXT,
        score INTEGER,
        grade TEXT
    )
""")

# Insert some dummy data
data = [
    (1, "Abby", "Math", 95, "A"),
    (2, "Liam", "Math", 78, "C"),
    (3, "Kyara", "Arts", 88, "B"),
    (4, "Kira", "History", 92, "A"),
    (5, "Sadie", "Science", 85, "B"),
    (6, "Rebecca", "Math", 65, "D")
]

cursor.executemany("INSERT OR IGNORE INTO grades VALUES (?, ?, ?, ?, ?)", data)
connection.commit()
connection.close()

print("Database created and populated successfully!")