import sqlite3

# Connect to the database
connection = sqlite3.connect("threat_detection.db")

cursor = connection.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS threat_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bytes INTEGER,
    packets INTEGER,
    result TEXT
)
""")

# Add sample detection records
cursor.execute(
    "INSERT INTO threat_logs (bytes, packets, result) VALUES (?, ?, ?)",
    (30000, 500, "Threat Detected")
)

cursor.execute(
    "INSERT INTO threat_logs (bytes, packets, result) VALUES (?, ?, ?)",
    (5000, 50, "Threat Detected")
)

connection.commit()

# Retrieve stored records
cursor.execute("SELECT * FROM threat_logs")

records = cursor.fetchall()

print("Stored Threat Detection Records:")
for record in records:
    print(record)

connection.close()

print("Data storage and retrieval completed!")