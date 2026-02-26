# Combine interns and mentors tables using INNER JOIN and load into Pandas
import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('interns.db')
cursor = conn.cursor()

# Create mentors table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS mentors (
        mentor_id INTEGER PRIMARY KEY AUTOINCREMENT,
        mentor_name TEXT NOT NULL,
        track TEXT NOT NULL
    )
''')

# Insert sample data into mentors table if empty
cursor.execute('SELECT COUNT(*) FROM mentors')
if cursor.fetchone()[0] == 0:
    mentors_data = [
        ('Dr. Smith', 'Data Science'),
        ('Ms. Johnson', 'Web Development'),
        ('Dr. Lee', 'AI')
    ]
    cursor.executemany('INSERT INTO mentors (mentor_name, track) VALUES (?, ?)', mentors_data)
    conn.commit()

# INNER JOIN query to display interns with their mentor for each track
join_query = '''
    SELECT i.intern_name, i.track, m.mentor_name
    FROM interns i
    INNER JOIN mentors m ON i.track = m.track
'''
df = pd.read_sql_query(join_query, conn)

print("Interns with their track's mentor:")
print(df)

conn.close()
import sqlite3
import pandas as pd

# Create in-memory SQLite database
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Create interns table
cursor.execute('''
CREATE TABLE interns (
    intern_id INTEGER PRIMARY KEY,
    intern_name TEXT,
    track TEXT
)
''')

# Insert data into interns
cursor.executemany('''
INSERT INTO interns VALUES (?, ?, ?)
''', [
    (1, 'Alice', 'Data Science'),
    (2, 'Bob', 'Web Development'),
    (3, 'Charlie', 'Data Science'),
    (4, 'David', 'Cyber Security')
])

# Create mentors table
cursor.execute('''
CREATE TABLE mentors (
    mentor_id INTEGER PRIMARY KEY,
    mentor_name TEXT,
    track TEXT
)
''')

# Insert data into mentors
cursor.executemany('''
INSERT INTO mentors VALUES (?, ?, ?)
''', [
    (1, 'Dr. Smith', 'Data Science'),
    (2, 'Ms. Johnson', 'Web Development'),
    (3, 'Mr. Lee', 'Cyber Security')
])

# Commit changes
conn.commit()

# INNER JOIN query
query = '''
SELECT 
    i.intern_name,
    i.track,
    m.mentor_name
FROM interns i
INNER JOIN mentors m
ON i.track = m.track;
'''

# Load result into Pandas DataFrame
df = pd.read_sql_query(query, conn)

# Display output
print(df)

# Close connection
conn.close()