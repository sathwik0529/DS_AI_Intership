import sqlite3

# Connect to the SQLite database (change the filename if needed)
conn = sqlite3.connect('interns.db')
cursor = conn.cursor()

# Create the interns table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS interns (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        track TEXT NOT NULL,
        stipend INTEGER NOT NULL
    )
''')

# Insert sample data if table is empty
cursor.execute('SELECT COUNT(*) FROM interns')
if cursor.fetchone()[0] == 0:
    sample_data = [
        ('Alice', 'Data Science', 6000),
        ('Bob', 'Web Development', 4500),
        ('Charlie', 'Data Science', 5200),
        ('David', 'AI', 7000),
        ('Eva', 'Web Development', 5500),
        ('Frank', 'Data Science', 4800),
        ('Grace', 'AI', 8000),
        ('Helen', 'Data Science', 5100)
    ]
    cursor.executemany('INSERT INTO interns (name, track, stipend) VALUES (?, ?, ?)', sample_data)
    conn.commit()

# 1. Filter: Data Science interns with stipend > 5000
print("Interns in 'Data Science' track with stipend > 5000:")
cursor.execute("""
    SELECT * FROM interns
    WHERE track = 'Data Science' AND stipend > 5000
""")
for row in cursor.fetchall():
    print(row)

# 2. Aggregate: Average stipend for each track
print("\nAverage stipend for each track:")
cursor.execute("""
    SELECT track, AVG(stipend) AS average_stipend
    FROM interns
    GROUP BY track
""")
for row in cursor.fetchall():
    print(row)

# 3. Count: Number of interns in each track
print("\nNumber of interns in each track:")
cursor.execute("""
    SELECT track, COUNT(*) AS intern_count
    FROM interns
    GROUP BY track
""")
for row in cursor.fetchall():
    print(row)

conn.close()
