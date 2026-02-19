import sqlite3

# Step 1: Connect to (or create) the database
conn = sqlite3.connect("internship.db")
cursor = conn.cursor()

# Step 2: Create the interns table
cursor.execute("""
CREATE TABLE IF NOT EXISTS interns (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    track TEXT NOT NULL,
    stipend REAL
)
""")

# Step 3: Insert 5 sample rows
intern_data = [
    (1, "Alice Johnson", "Data Science", 1500),
    (2, "Bob Smith", "Web Dev", 1200),
    (3, "Carol White", "Cybersecurity", 1400),
    (4, "David Brown", "Data Science", 1600),
    (5, "Eva Green", "Web Dev", 1300)
]

cursor.executemany("""
INSERT OR REPLACE INTO interns (id, name, track, stipend)
VALUES (?, ?, ?, ?)
""", intern_data)

conn.commit()

# Step 4: Query only name and track
cursor.execute("SELECT name, track FROM interns")

results = cursor.fetchall()

# Step 5: Display results
print("Intern Name and Track:")
for row in results:
    print(f"Name: {row[0]}, Track: {row[1]}")

# Close connection
conn.close()
