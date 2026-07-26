import os
import sqlite3
import pandas as pd

db_path = 'data/nifty100.db'
if os.path.exists(db_path):
    os.remove(db_path)

conn = sqlite3.connect(db_path)

# Load database loader module
import database.load_to_db

print("Checking loaded tables...")
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables successfully written:", [t[0] for t in tables])
conn.close()
